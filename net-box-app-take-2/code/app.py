from flask import Flask, jsonify
from flask_restful import Resource, reqparse, request, Api
from flask_sqlalchemy import SQLAlchemy
from resources.tool import Tool


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/glitch/Documents/pythonRelated/network-toolbox-take-2/database/database.db'

db = SQLAlchemy(app)


    



@app.route("/")
def home():
  return render_template("index.html")




api.add_resource(Tool, '/tool')




if __name__=='__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')

