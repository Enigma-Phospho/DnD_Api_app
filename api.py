from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#setting up flask app
app = Flask(__name__)

#setting up SQL alchemy
#The database URI that should be used for the connection.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////party.db'
db = SQLAlchemy(app)

# Define the class for the party table
# The model class defines a new Kind of datastore entity and the 
# properties the Kind is expected to take.
# The Kind name is defined by the instantiated class name that inherits 
# from db.Model.  
class Party_mem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cls = db.Column(db.String)
    rce = db.Column(db.String)
    stren = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    const = db.Column(db.Interger)
    intel = db.Column(db.Integer)
    wizd = db.Column(db.Integer)
    charis = db.Column(db.Integer)

# create table
db.create_all