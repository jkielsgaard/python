from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GetData(Resource):
    def get(self):
        return { "Value" : "Hello Bit World" }

api.add_resource(GetData, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)