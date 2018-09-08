import json
import utils

def get():
    return utils.load_json_file('taxis_results.json')

# def post():
#     return utils.load_json_file('flight-offers-post.json')