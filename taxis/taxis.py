import json
import utils

def get(city=None, taxi_id=None):
    if city and taxi_id:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if (taxi['city'] == city and taxi['name'] == taxi_id)]
        return {"meta":{"count":0,"links":{"self":"https://mock-travel-apis.herokuapp.com/taxis"}},"data":results}
    elif city:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if taxi['city'] == city]
        return {"meta":{"count":0,"links":{"self":"https://mock-travel-apis.herokuapp.com/taxis"}},"data":results}
    else:
        return utils.load_json_file('taxis.json')

# def post():
#     return utils.load_json_file('flight-offers-post.json')