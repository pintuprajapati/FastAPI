# FastAPI
Practicing FastAPI

How to run this API locally:

## Installation
- Create a `virtualenv` and **activate** it.
- Install the **requirements.txt** file `pip3 install -r requirements.txt`
  - To check uvicorn version: `uvicorn --version`
  
## Run locally
 
- **Command to run the FastAPI server:** `uvicorn main:app --reload`
    - Here
        - `main` is our filename `main.py`
        - `app` is our instance which we created in code `app = FastAPI()`
        - If we change the ******************************************instance and filename****************************************** to something else then we have to use those to run the server
    - since we added `--reload` command at the end, after every save, it will be **reloaded** automatically and changes will be affected
    
## Output in Normal JSON Format
- Check the output in browser: usually at ********8000******** port
    - [`http://localhost:8000/`](http://localhost:8000/)
    - [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)
    - [`http://127.0.0.1:8000/about`](http://127.0.0.1:8000/about)
    
## Output in Swagger UI in Browswer
- [`http://localhost:8000/docs`](http://localhost:8000/docs)
- [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
