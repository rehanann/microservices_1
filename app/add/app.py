from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Add(Resource):
      def post(self):
            postedData = request.get_json()
            num1 = postedData["num1"]
            num2 = postedData["num2"]
            num1 = int(num1)
            num2 = int(num2)

            add_ret = num1 + num2
            addMap = {
              'Result' : add_ret,
              'Status' : 200
            }
            return jsonify(addMap)

api.add_resource(Add, "/add")


if __name__ == '__main__':
      app.run(host='0.0.0.0')

