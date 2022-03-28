from flask import Flask

app = Flask(__name__)

# TODO: Create a Flask REST-API with:
#  User model, auth
#  Posts model, create/update/delete posts
#  Comments thread
#  README.md


@app.route('/')
def hello():
    return 'Hello, World!'
