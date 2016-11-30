from flask import Flask, request
from flask_restful import Api

from .api.base import BaseApi
from .api import api_list

from .models import database

app = Flask(__name__)
api = Api(app)

api.add_resource(BaseApi, BaseApi.endpoint)

for api_class in api_list:
	api.add_resource(api_class, api_class.endpoint)


def mmap_reset():
    database.rollback()
