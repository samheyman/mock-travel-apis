import json
import utils

def get(city=None, id=None):
    if city and id:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if (taxi['city'] == city and taxi['name'] == id)]
        return {"meta":{"count":0,"links":{"self":"https://mock-travel-apis.herokuapp.com/taxis"}},"data":results}
    elif city:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if taxi['city'] == city]
        return {"meta":{"count":0,"links":{"self":"https://mock-travel-apis.herokuapp.com/taxis"}},"data":results}
    else:
        return utils.load_json_file('taxis_results.json')

# def post():
#     return utils.load_json_file('flight-offers-post.json')