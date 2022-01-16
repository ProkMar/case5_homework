#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:38:37 2022

@author: prokmar
"""

import requests

service_host = 'localhost'
service_port = 5110

# type_request = 'train'
type_request = 'predict'

url = f'http://{service_host}:{service_port}/{type_request}'

s = requests.session()

if type_request == 'predict':

    params = {
        'sepal_length': 10,
        'sepal_width': 3,
        'petal_length': 8,
        'petal_width': 4
        }

    response = s.post(url, json=params)

else:

    response = s.get(url)

print(url)
print(response.text)
