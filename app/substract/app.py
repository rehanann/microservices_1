from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Substract(Resource):
      def post(self):
            postedData = request.get_json()
            num1 = postedData["num1"]
            num2 = postedData["num2"]
            num1 = int(num1)
            num2 = int(num2)

            sub_ret = num1 - num2
            subMap = {
              'Result' : sub_ret,
              'Status' : 200
            }
            return jsonify(subMap)

api.add_resource(Substract, "/substract")


if __name__ == '__main__':
      app.run(host='0.0.0.0')

