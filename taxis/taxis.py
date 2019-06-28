import json
import utils

def get(city=None, taxi_id=None):
    if city and taxi_id:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if (taxi['city'] == city and taxi['name'] == taxi_id)]
        number_results = len(results)
        return {"meta":{"count":number_results,"links":{"self":"https://mock-travel-apis.herokuapp.com/taxis/"+city+"/"+taxi_id}},"data":results}
    elif city:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if taxi['city'] == city]
        number_results = len(results)
        return {"meta":{"count":number_results,"links":{"self":"https://mock-travel-apis.herokuapp.com/taxis/"+city}},"data":results}
    else:
        return utils.load_json_file('taxis.json')

# def post():
#     return utils.load_json_file('flight-offers-post.json')