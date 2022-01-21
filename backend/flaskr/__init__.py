from crypt import methods
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from random import randint
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(page, questions):
  """ Formats and paginate the given list of questions according to the given page number
    page <int>: the page numver
    questions <list<Question>>: list of Question objects
    Retutns: list of dictionaries
  """
  start_index = (page - 1) * QUESTIONS_PER_PAGE
  questions = [q.format() for q in questions]
  return questions[start_index: start_index + QUESTIONS_PER_PAGE]


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  CORS(app, resources={r"*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    response.headers.add("Acess-Control-Allow-Headers",
                          "Content-Type, Authorization")
    response.headers.add("Acess-Control-Allow-Methos",
                          "GET, POST, DELETE")
    
    return response

  @app.route("/categories", methods=["GET"])
  def categories():
    # Get categories then format them in id:type pairs
    categories = Category.query.order_by(Category.id).all()
    id_to_type_dict = {}
    for c in categories:
      id_to_type_dict[c.id] = c.type
    
    return jsonify({
      "success": True,
      "categories": id_to_type_dict,
      "total_categories": len(categories) 
    })

  @app.route("/questions", methods=["GET", "POST"])
  def questions(category = "all"):
    if request.method == "GET": 
      # if category is set to default ("all") then return all questions
      if category == "all":
        questions = Question.query.order_by(Question.id).all()
      else:  # if category isn't set to "all" return questions in the given category
        if not Category.query.filter_by(id=category).first():  # if Category doesn't exits raise an error
          abort(404)
        questions = Question.query.filter_by(category=category).order_by(Question.id).all()
      
      # Get the page number from url query parameters, if it doesn't exist set the page number to 1
      page = request.args.get("page", 1, type = int)

      return jsonify({
        "success": True,
        "questions": paginate_questions(page, questions),
        "total_questions": len(questions),
        "current_category": category,
        "categories": categories().json["categories"]
      })
    
    else: #run if the request method is not GET. which means it's POST 
      data = request.json
      #if the POST request doesn't have a body raise bad reques error
      if not data:
        abort(400)
      # if the request body have searchTerm key
      if data.get("searchTerm", None):
        # get the search term from the body
        search_term = data["searchTerm"].strip()
        # get questions that match the search term and return them
        resault = Question.query.filter(Question.question.ilike(f"%{search_term}%")).all()
        return jsonify({
          "success": True,
          "questions": [q.format() for q in resault]
        })
     
      else:  # create new question
        try:
          question_string = data["question"].strip()
          answer = data["answer"].strip()
          category = data["category"]
          difficulty = data["difficulty"]
          if question_string == "" or answer == "":
            # if the body has an empty question or answer then raise unprocessable entity error
            abort(422)
        except:
          # if the body doesn't contain all the required data raise bad request error
          abort(400)
        
        # create the question and add it to the database
        question = Question(question_string, answer, category, difficulty)
        question.insert()
        return jsonify({
          "success": True,
          "created": question.id
        })

  @app.route("/questions/<id>", methods = ["DELETE"])
  def individual_question(id):
    question = Question.query.filter_by(id=id).first()
    if not question:
      # if the question doesn't exist return unprocessable entity error
      abort(422)
    
    question.delete()
    return jsonify({
      "success": True,
      "deleted": id
    })

  @app.route("/categories/<id>/questions", methods=["GET"])
  def category_questions(id):
    return questions(id)

  @app.route("/quizzes", methods=["POST"])
  def quiz():
    try:
      data = request.json
      previous_questions = data["previous_questions"]
      quiz_category_id = data["quiz_category"]["id"]
    except:
      # if the request doesn't have the required data raise bad request error
      abort(400)
    
    # get the category and if doesn't exist then get question from all the categories
    category = Category.query.filter_by(id=quiz_category_id).first()
    if category:
      questions = Question.query.filter_by(category=category.id).all()
    else:
      questions = Question.query.all()

    # remove the previous questions from the questions list
    i = 0
    while i < len(questions):
      if questions[i].id in previous_questions:
        del questions[i]
        i-=1
      i+=1

    # if the questions list still has elements then choose a random question and return it
    if len(questions) == 0:
      random_question = ""
    else:
      random_question = questions[randint(0, len(questions)-1)].format()
    return jsonify({
      "success": True,
      "question": random_question
    })

  
  #-----------------------------------
  #           Error handlers
  #-----------------------------------
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "not found"
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422

  @app.errorhandler(405)
  def not_allowed_method(error):
    return jsonify({
      "success": False,
      "error": 405,
      "message": "method not allowed"
    }), 405

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "internal server error"
    }), 500

  return app
