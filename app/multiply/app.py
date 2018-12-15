from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Multiply(Resource):
      def post(self):
            postedData = request.get_json()
            num1 = postedData["num1"]
            num2 = postedData["num2"]
            num1 = int(num1)
            num2 = int(num2)

            mul_ret = num1 * num2
            mulMap = {
              'Result' : mul_ret,
              'Status' : 200
            }
            return jsonify(mulMap)

api.add_resource(Multiply, "/multiply")


if __name__ == '__main__':
      app.run(host='0.0.0.0')

