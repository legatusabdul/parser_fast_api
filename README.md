# parser_fast_api


This application scrapes pypi package information by keyword and downloads it in a csv file on the user's device
### FastAPI, bootstrap 5

----

## Local Run

### Run python FastAPI app

- Create virtual environment and activate it
    ```python
    > python -m venv venv
    > source venv/bin/activate
    ```
- install all dependencies:
    ```
    (venv) pip install -r requirements.txt
    ```    
- go to app directory
    ```
    (venv) > cd app
    ```
- run FastAPI application:
    ```
    uvicorn main:app --reload
    ```
### You can open the application in your browser

- `http://127.0.0.1:8000`