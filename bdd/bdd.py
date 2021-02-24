import pytest
import requests
import json
from pytest_bdd import scenarios, when, then


param = {
	'access_key':'058d6f074fad58d126c6d9851fcb8d2e',
	'query' : 'Saint Louis',
}

# api_response = api_result.json()
# json_results = open("weather_data.json", "w")
# json.dump(api_response, json_results)


@when("Open weatherstacks website")
def weather_response(param):
	response = requests.get('http://api.weatherstack.com/current', param)
	return response

@then("the weather response shoes different weather data points")
def weather_response_name(weather_response, city_name):
	assert city_name == weather_response.json()['query']

@then('the response status code is 200')
def weather_response_code(weather_response):
	assert weather_response.status_code == 200