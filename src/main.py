from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#defining requests
class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

api.add_resource(HelloWorld, "/helloworld")

#start our application
if __name__ == "__main__":
    app.run(debug=True)