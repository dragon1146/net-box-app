from flask import Flask, redirect, url_for, render_template
from flask_restful import Resource, Api, reqparse
# from flask_jwt import JWT, jwt_required

# from security import authenticate, identity
# from resources.user import UserRegister  
from resources.task import Task



app = Flask(__name__)
api = Api(app)


@app.route("/")
def home():
  return render_template("index.html")



# app.secret_key = 'jose'

# jwt = JWT(app, authenticate, identity)



api.add_resource(Task, '/task/<string:task>')



# api.add_resource(Itemlist, '/items')
# api.add_resource(UserRegister, '/register')

# debug=True will allow the source of the API to be updated and synced without restarting the API
if __name__=='__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')