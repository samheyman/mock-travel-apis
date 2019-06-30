from bottle import run, post, request, response, get, route
import os
import json
import utils
from taxis import taxis


@get('/taxis')
def get_taxis():
    return taxis.get()

@get('/taxis/<city>')
def get_taxis_city(city):
    return taxis.get(city=city)

@get('/taxis/<city>/<taxi_id>')
def get_taxi_city(city, taxi_id):
    return taxis.get(city=city, taxi_id=taxi_id)

@post('/taxis/<city>/<taxi_name>')
def get_taxi_city(city, taxi_name):
    return taxis.post(city=city, taxi_name=taxi_name)


if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
