import json
import utils
import time

def get(city=None, taxi_id=None):
    if city and taxi_id:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if (taxi['city'] == city and taxi['name'] == taxi_id)]
        print(results)
        number_results = len(results)
        response = {
            "meta": {
                "count":number_results,
                "links":{
                    "self":"https://mock-travel-apis.herokuapp.com/taxis/"+city+"/"+taxi_id
                },
            },
            "data":results
        }
        return json.dumps(response)
    elif city:
        filedata = utils.load_json_file('taxis.json')["data"]
        results = [taxi for taxi in filedata if taxi['city'] == city]
        number_results = len(results)
        response = {
            "meta":{
                "count":number_results,
                "links":{
                    "self":"https://mock-travel-apis.herokuapp.com/taxis/"+city
                },
            },"data":results
        }
        return json.dumps(response)
    else:
        return utils.load_json_file('taxis.json')

def post(city=None, taxi_name=None):
    if city and taxi_name:
        filedata = utils.load_json_file('taxis.json')
        taxi_info = {}
        for taxi in filedata["data"]:
            if taxi["name"] == taxi_name:
                print("Found taxi!")
                taxi["state"] = "hired" if taxi["state"] == "free" else "free"
                print(taxi)
                taxi_info = taxi
        utils.save_json_file(filedata, 'taxis.json')
        response = {
            "meta":{
                "count":1,
                "links":{
                    "self":"https://mock-travel-apis.herokuapp.com/taxis/"+taxi_info["city"]+"/"+taxi_info["name"]
                },
            },
            "data":taxi_info
        }
        return json.dumps(response)
    else:
        return "Could not book taxi"
    
