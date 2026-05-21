from fastapi import FastAPI


# Create an object (instance) of FastAPI
# This object will be our main application
app = FastAPI()


# ------------------------------
# Route: "/"
# ------------------------------
# @app.get("/") means:
# When someone visits the homepage URL using a GET request,
# run the function written below it.
#
# Example:
# http://127.0.0.1:8000/
#
# GET request is mainly used to fetch/read data.
@app.get("/")

# Function that will run when the "/" route is accessed
def hello():

    # Return data in dictionary format
    # FastAPI automatically converts this dictionary into JSON
    #
    # Output in browser/API response:
    # {
    #     "message": "hello world"
    # }
    return {"message": "hello world"}

@app.get('/about')
def about():
    return {
        'message' : 'aryan Chaudhari'
    }