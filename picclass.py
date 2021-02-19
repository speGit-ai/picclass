import sys


import json
import base64
import requests


def Pic(path):
    appid = ''
    client_id = ''
    client_secret = ''
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials'
    host += "&client_id=%s&client_secret=%s" % (client_id, client_secret)

    session = requests.Session()
    response = session.get(host)
    access_token = response.json().get("access_token")

    request_url = ""
    with open(path, 'rb') as f:
        image = base64.b64encode(f.read()).decode('UTF8')
    headers = {
    'Content-Type': 'application/json'
    }
    params = {
    "image": image
    }
    request_url = request_url + "?access_token=" + access_token
    response = session.post(request_url, headers=headers, json=params)
    content = response.content.decode('UTF-8')
    results = json.loads(content)     #json转为字典



    #print(results)
    classifi = results['results'][0]['name']
    print(classifi)

    return classifi
