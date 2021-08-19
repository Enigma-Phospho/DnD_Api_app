from abstr_lyr import TraitsSchema
from flask_rest_jsonapi import ResourceList
from flask_rest_jsonapi import ResourceList
from api import Schema
from api import Traits
from api import db 

# Resource management system using resource list for retrieval of items 
class TraitsList (ResourceList):
    schema = TraitsSchema
    data_layer = {'session': db.session,
                  'model': Traits}

