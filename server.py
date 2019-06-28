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

@get('/taxis/<city>/<id>')
def get_taxi_city(city, id):
    return taxis.get(city=city, id=id)


if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
