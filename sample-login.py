from __init__ import executeget
from __init__ import executelogin
from __init__ import config
import json

# Security Login/Logout

if not config['Global']['api.authToken']:
    ## Please set the config['Global']['api.username'] and config['Global']['api.password'] in __init__.cfg
    print("Using login with user/password")
    login_result = executelogin(username=config['Global']['api.username'],
                                password=config['Global']['api.password'])

else:
    ## Please set the config['Global']['api.authToken'] in __init__.cfg
    login_result = executelogin(authToken=config['Global']['api.authToken'])

config['Global']['api.token'] = login_result['data']['access-token']
print(f"Login access-token: {config['Global']['api.token']}")
print("Response")
print(json.dumps(login_result, indent=4))

print(json.dumps(executeget("/security/logout"), indent=4))