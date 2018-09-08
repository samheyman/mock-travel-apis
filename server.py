
from bottle import run, post, request, response, get, route
import os
import json
import utils
import taxis.taxis


@get('/taxis')
def get_taxis():
    return taxis.taxis.get()
    
if __name__ == "__main__":

    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
