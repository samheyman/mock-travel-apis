# Mock Travel APIs

Mock travel APIs to use to stub out the real APIs.

## Demo

### Taxis
* [GET /taxis](https://mock-travel-apis.herokuapp.com/taxis) - a list of all taxis
* [GET /taxis/\<city\>]() - a list of all taxis in a city
* [GET /taxis/\<city\>/\<taxi_id\>]() - details for a given taxi

## Usage

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What you will need:

* python 3.6
* virtualenv
* pip

### Installing

To run it locally:

* install the requirements
```
pip install -r requirements.txt
```
* run the server
```
python server.py
```
* you can access the API here:
```
localhost:8080/taxis
```


## Built With

* [Bottle](https://bottlepy.org/docs/dev/) - A simple WSGI micro web-framework for Python


## Authors

* *Initial work* - [SamHeyman](http://samheyman.com)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

With contribution from:
* [Alvaro Navarro](https://github.com/alnacle)
* [Anthony Roux](https://github.com/anthonyroux)
