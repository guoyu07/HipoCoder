# encoding=utf-8
__author__ = 'Jack'

import requests
import json

url = 'https://api.github.com/authorizations'
note = 'Github access'
post_data = {'scopes':['repo','user'],'note':note}

username = 'latexers@gmail.com'
passowrd = '19880928wang'
response = requests.post(
    url,
    auth = (username, passowrd),
    data = json.dumps(post_data),
)

print "API response:", response.text
print
print "Your OAuth token is",response.json()['token']