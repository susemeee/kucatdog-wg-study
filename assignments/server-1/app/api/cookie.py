from app.api.base import BaseApi
from app.models import database
from flask import request
from flask_restful import reqparse
import json

#parser = reqparse.RequestParser()

cookie_types = ['strawberry', 'zombie', 'apple', 'mint', 'peach']

def check_data(data):
    if not 'flavor' in data or not 'size' in data:
        return False

def check_cookie(data):

    if not (int(data['size']) >= 10 and int(data['size']) <= 30):
        return False

    if not data['flavor'] in cookie_types:
        return False

    return True

class CookieApi(BaseApi):
    endpoint = '/cookie/<string:cookie_name>'

    def get(self, cookie_name):

        data = request.get_data().decode('utf-8')
        null_dict = dict([])

        if data != ""  and request.form == null_dict:
            return False, 400

        if not cookie_name in database:
            return False, 404


        return database[cookie_name]

    def post(self, cookie_name):
        return False, 400

    def put(self, cookie_name):

        data = request.get_data().decode('utf-8')
        null_dict = dict([])

        #print(data)
        #print(request.args)
        #print(request.form)

        if data != "" and request.form == null_dict:
            return False, 400

        if not cookie_name in database:
            return False, 404

        if check_data(request.form) == False:
            return False, 400

        if check_cookie(request.form) == False:
            return False, 422

        database[cookie_name] = {
        'flavor' : request.form['flavor'],
        'size' : int(request.form['size'])
        }

        return cookie_name

    def delete(self, cookie_name):

        data = request.get_data().decode('utf-8')
        null_dict = dict([])

        if data != ""  and request.form == null_dict:
            return False, 400

        if not cookie_name in database:
            return False, 404
        
        del database[cookie_name]

        return True

class CookieListApi(BaseApi):
    endpoint = '/cookie/'
    cookie_count = 0

    def get(self):
        return list(database.keys())

    def post(self):

        data = request.get_data().decode('utf-8')
        null_dict = dict([])
        #print(request.form)
        #print(request.get_data())

        if data != "" and request.form == null_dict:
            return False, 400

        if check_data(request.form) == False:
            return False, 400

        if check_cookie(request.form) == False:
            return False, 422

        CookieListApi.cookie_count += 1
        database[str(CookieListApi.cookie_count)] = {
        'flavor' : request.form['flavor'],
        'size' : int(request.form['size'])
        }

        print(database[str(CookieListApi.cookie_count)])
        print(CookieListApi.cookie_count)

        return {"id" : str(CookieListApi.cookie_count)}
