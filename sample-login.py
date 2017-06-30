from __init__ import executeget
from __init__ import executelogin
from __init__ import config

# Security Login/Logout

## Please set the config['Global']['api.username'] and config['Global']['api.password'] in __init__.cfg
print (executelogin(username=config['Global']['api.username'],
                   password=config['Global']['api.password']))

## Please set the config['Global']['api.authToken'] in __init__.cfg
print(executelogin(authToken=config['Global']['api.authToken']))

print(executeget("/security/logout"))