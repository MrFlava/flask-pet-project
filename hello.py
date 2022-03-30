import json
from flask import Flask
from flask_restful import Resource, Api

# from .models import Users

app = Flask(__name__)
api = Api(app)

# TODO: Create a Flask REST-API with:
#  User model, auth
#  Posts model, create/update/delete posts
#  Comments thread
#  README.md


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
