import requests
import os


def get_details_imdb(name):
    API_KEY = os.environ.get('API_KEY')
    payload = {'t': name, 'apikey': API_KEY}
    return requests.get('https://www.omdbapi.com/', params=payload).json()


