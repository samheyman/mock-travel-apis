import unittest
from unittest.mock import patch
from context import taxis
import json

class TestTaxis(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_all_taxis(self):
        all_taxis_response = taxis.get()
        self.assertEqual(2, len(all_taxis_response), "Response did not contain the 2 objects: 'meta' and 'data'")
        self.assertEqual(4, len(all_taxis_response["data"]), "Response data object did not contain the correct number of taxis (4)")
        self.assertEqual('hyundai', all_taxis_response["data"][0]["name"])
        self.assertIn('city', all_taxis_response["data"][0], "The taxi object did not contain the city element")

    def test_taxis_in_city(self):
        taxis_response = json.loads(taxis.get(city='paris'))
        self.assertEqual('peugeot', taxis_response["data"][0]["name"])

    def test_taxi_in_city(self):
        taxis_response = json.loads(taxis.get(city='paris', taxi_id="peugeot"))
        self.assertEqual('peugeot', taxis_response["data"][0]["name"])

    def test_book_taxi(self):
        taxis_response = json.loads(taxis.post(city='barcelona', taxi_name="fiat"))
        self.assertEqual('fiat', taxis_response["data"]["name"])

    def test_booking_unsuccessful(self):
        taxis_response = taxis.post(city='moscow', taxi_name="")
        print(taxis_response)
        self.assertEqual('Could not book taxi', taxis_response)

    def test_no_taxis(self):
        taxis_response = json.loads(taxis.get(city='moscow'))
        self.assertEqual(0, taxis_response["meta"]["count"])
    

if __name__ == '__main__':
    unittest.main()