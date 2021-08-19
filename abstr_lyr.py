from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

# Logical Abstraction 
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
