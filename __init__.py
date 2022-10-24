import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('__init__.cfg')

CONNECTION_URL_PREFIX = config['Global']['api.protocol'] + '://' + \
                        config['Global']['api.server.url'] + ':' + \
                        config['Global']['api.server.port'] + '/api/' + \
                        config['Global']['api.version']

def executeget( path , param={}):
    response = requests.get(CONNECTION_URL_PREFIX + path,
                            params=param,
                            headers={"Content-Type":"applicaiton/json",
                                     "Access-Token":config['Global']['api.token']})
    if response.status_code == 200:
       return json.loads(response.content)
    else:
        print(f'request failed: {response.content}')
    return

def executelogin( username="", password="", authToken=""):
    json_data = {}
    if not authToken:
        json_data = {"username":username, "pwd":password}
    else:
        json_data = {"authToken":authToken}
    response = requests.post(CONNECTION_URL_PREFIX + '/security/login',
                             data=json_data,
                             headers={"Content-Type":"application/x-www-form-urlencoded"})
    if response.status_code == 200:
        return response.json()
    else:
        print(f'request failed: {response.content}')
    return

def executepost( path , data={}):
    response = requests.post(CONNECTION_URL_PREFIX + path,
                             json=data,
                             headers={'Content-Type':'application/json',
                                      "Access-Token": config['Global']['api.token']})
    if response.status_code == 200:
        return response.json()
    else:
        print(f'request failed: {response.content}')
    return

def transformjson ( content = ""):
    return json.loads(json.dumps(content))

