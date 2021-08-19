from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_rest_jsonapi import Api

#setting up flask app
app = Flask(__name__)

#setting up API and routing
api = Api()
api.route(TraitsList, 'traits_list', '/traits')

#setting up SQL alchemy
#The database URI that should be used for the connection.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////party.db'
db = SQLAlchemy(app)

# Define the class for the party table
class Traits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    race = db.Column(db.String)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Interger)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)





# create table
db.create_all


