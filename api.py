from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow.fields import Integer
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema
from sqlalchemy.orm import load_only


#setting up flask app
app = Flask(__name__)


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

# Logical Abstraction for build/trait data
class TraitsSchema(Schema):
    class Meta: 
        type_ = 'Traits'
        self_view = 'Traits_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'traits_list'
    
    id = fields.Integer(as_string=True, load_only=True)
    clas = fields.String(required=True, load_only=True)
    race = fields.String(required=True)
    strength = fields.Integer(as_string=True, load_only=True)
    dexterity = fields.Integer(as_string=True, load_only=True)
    constitution = fields.Integer(as_string=True, load_only=True)
    intelligence = fields.Integer(as_string=True, load_only=True)
    wisdom = fields.Integer(as_string=True, load_only=True)
    charisma = fields.Integer(as_string=True, load_only=True)
    
# create table
db.create_all
