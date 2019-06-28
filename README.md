# Mock Travel APIs

Mock travel APIs to use to stub out the real APIs.

## Demo

### Taxis

* [GET /taxis](https://mock-travel-apis.herokuapp.com/taxis) - a list of all taxis
```shell
{
	"meta":{
		"count": 2,
		"links":{
			"self": "https://mock-travel-apis.herokuapp.com/taxis"
		}
	},
	"data":[
		{
			"state": "free",
			"name": "hyundai",
			"location": {
				"lon": 3.703,
				"lat": 40.41
			},
			"city": "madrid"	
		},
		{
			"state": "free",
			"name": "fiat",
			"location": {
				"lon": 2.1734,
				"lat": 41.38
			},
			"city": "barcelona"	
		},
        ...
    ]
}
```
* [GET /taxis/\<city\>]() - a list of all taxis in a city
```shell
{
	"meta":{
		"count": 2,
		"links":{
			"self": "https://mock-travel-apis.herokuapp.com/taxis"
		}
	},
	"data":[
		{
			"state": "free",
			"name": "hyundai",
			"location": {
				"lon": 3.703,
				"lat": 40.41
			},
			"city": "madrid"	
		},
		{
			"state": "free",
			"name": "fiat",
			"location": {
				"lon": 3.732,
				"lat": 40.51
			},
			"city": "madrid"	
		},
        ...
    ]
}
```
* [GET /taxis/\<city\>/\<taxi_id\>]() - details for a given taxi
```shell
{
	"meta":{
		"count": 1,
		"links":{
			"self": "https://mock-travel-apis.herokuapp.com/taxis"
		}
	},
	"data":[
		{
			"state": "free",
			"name": "hyundai",
			"location": {
				"lon": 3.703,
				"lat": 40.41
			},
			"city": "madrid"	
		},
        ...
    ]
}
```
* [POST /taxis/\<city\>/\<taxi_id\>]() - book a given taxi
```shell
{
	"meta":{
		"count": 1,
		"links":{
			"self": "https://mock-travel-apis.herokuapp.com/taxis"
		}
	},
	"data":[
		{
			"state": "hired",
			"name": "hyundai",
			"location": {
				"lon": 3.703,
				"lat": 40.41
			},
			"city": "madrid"	
		},
        ...
    ]
}
```

## Usage

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What you will need:

* python 3.6
* pip
* pipenv

### Installing

To run it locally:

* install the requirements
```
pipenv install
```
* run the server
```
pipenv run python server.py
```
* you can call the API with the following requests:
```
GET localhost:8080/taxis
GET localhost:8080/taxis/madrid
GET localhost:8080/taxis/madrid/hyundai
POST localhost:8080/taxis/madrid/hyundai

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
