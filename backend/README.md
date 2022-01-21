# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.



# Getting Started
## Base URL
Currently this app can only be hosted locally. The backend app is hosted at the default:
`http://127.0.0.1:5000/`

## Endpoints
### GET /categories
- **Description**: Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    - Returns: An object that contains:
        - `"categories"` **object** of `id : category_string` key:value pairs.
        - `"total_categories"` **integer**
        - `"success"` **boolean**
- **Sample**: `curl http://127.0.0.1:5000/categories`
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true,
    "total_categories": 6
}
```
### GET /questions
- **Description**: Fetches a dictionary of all the questions paginated in groups of 10  
    > The page can be chosen by using the query parameter `page` 
    - Returns: An object that contains:
        - `"questions"` **list** of **objects** that contain: 
            - `"id"` **integer**
            - `"question"` **string**
            - `"answer"` **string**
            - `"category"` **integer**
            - `"difficulty"` **integer**
        - `"categories"` **object** of `id : category_string` key:value pairs.
        - `"total_questions"` **integer** | The number of total questions in the  current category
        - `"success"` **boolean**
        - `"current_category"` The value can be either the id of the current category or the string "all"
        > **_NOTE:_**  The value of `"current_category"` will always be "all" when getting questions from this endpoint.

- **Sample**: `curl  http://127.0.0.1:5000/questions?page=1`
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": "all",
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "total_questions": 20
}
```
### GET /categories/{category_id}/questions
- **Description**: Fetches a dictionary of all the  questions in a certain category paginated in groups of 10  
    > The page can be chosen by using the query parameter `page`

    - Returns: An object that contains:
        - `"questions"` **list** of **objects** that contain: 
            - `"id"` **integer**
            - `"question"` **string**
            - `"answer"` **string**
            - `"category"` **integer**
            - `"difficulty"` **integer**
        - `"categories"` **object** of `id : category_string` key:value pairs.
        - `"total_questions"` **integer** | The number of total questions in the current category
        - `"success"` **boolean**
        - `"current_category"` **integer** | The id of the current category
- **Sample**: `curl http://127.0.0.1:5000/categories/2/questions`
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": "2",
    "questions": [
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
    ],
    "success": true,
    "total_questions": 2
}
```
### POST /questions
- **Description**: This endpoint can be used to either:
    - **Create** a new question 
        - Request Body: An object that contains the question data
            - `"question"` **string**
            - `"answer"` **string**
            - `"category"` **integer**
            - `"difficulty"` **integer**

        - Returns: An object that contains:
            - `"created"` **integer** | The id of the created question
            - `"success"` **boolean**
    - **Create Sample**: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"test", "answer":"test", "category":"1", "difficulty":"5"}'`
    ```
    {
        "success": True,
        "created": "21"
    }
    ```
    - **Search** for a question which will fetche all the questions that match the search term 
        - Request Body: An object that contains the search term
            - `"searchTerm"` **string**
    
        - Returns: An object that contains:
            - `"questions"` **list** of **objects** that contain: 
                - `"id"` **integer**
                - `"question"` **string**
                - `"answer"` **string**
                - `"category"` **integer**
                - `"difficulty"` **integer**
            - `"success"` **boolean**

    - **Search Sample**: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"La Giaconda"}'`
    ```
    {
        "questions": [
            {
                "answer": "Mona Lisa",
                "category": 2,
                "difficulty": 3,
                "id": 17,
                "question": "La Giaconda is better known as what?"
            }
        ],
        "success": true
    }
    ```

### DELETE /questions/{question_id}
- **Description**: Deletes a question from the database using its id
    - Returns: An object that contains:
        - `"deleted"` **integer** | The id of the deleted question
        - `"success"` **boolean**
- **Sample**: `curl http://127.0.0.1:5000/questions/5 -X DELETE`
```
{
    "success": True,
    "deleted": 5
}
```
### POST /quizzes/
- **Description**: Fetches random not repeating questions from certain category
    - Request Body: An object that contains the ids of the previous questions and the category id
        - `"previous_questions"` **list[integer]**
        - `"quiz_category"` **integer**

    - Returns: An object that contains:
        - `"question"` **object** That contains: 
            - `"id"` **integer**
            - `"question"` **string**
            - `"answer"` **string**
            - `"category"` **integer**
            - `"difficulty"` **integer**
        - `"success"` **boolean**
- **Sample**: `curl http://127.0.0.1:5000/quizzez -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20,21], "quiz_category": {"type": "Science", "id": "1"}}'`
```
{
    "question": {
        "answer": "Blood",
        "category": 1,
        "difficulty": 4,
        "id": 22,
        "question": "Hematology is a branch of medicine involving the study of what?"
    },
    "success": true
}
```
## Error Handling
The API uses default http error codes and returns errors as JSON objects  
### **Sample**:
```
{
    "error": 404,
    "message": "not found",
    "success": false
}
```

# Testing
To setup the tests, run:
```
createdb trivia_test
psql trivia_test < trivia.psql
```
Then run this every time you want to test the api
```
python test_flaskr.py
```