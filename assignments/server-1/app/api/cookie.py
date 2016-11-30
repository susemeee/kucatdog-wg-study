from app.api.base import BaseApi
from app.models import database
from flask import request
from flask_restful import reqparse
import json

#parser = reqparse.RequestParser()

class CookieApi(BaseApi):
    endpoint = '/cookie/<string:cookie_name>'

    def get(self, cookie_name):

        return database[cookie_name]

    def put(self, cookie_name):

        database[cookie_name] = {
        'flavor' : request.form['flavor'],
        'size' : request.form['size']
        }

        return cookie_name

    def delete(self, cookie_name):
        
        database[cookie_name] = None

        return True

class CookieListApi(BaseApi):
    endpoint = '/cookie'
    cookie_count = 0

    def get(self):
        return database

    def post(self):
        #args = parser.parse_args()
        CookieListApi.cookie_count += 1
        database[str(CookieListApi.cookie_count)] = {
        'flavor' : request.form['flavor'],
        'size' : request.form['size']
        }

        return CookieListApi.cookie_count
