import json
from . import user

def handle_user(function, args):
    if function == 'get_users':
        return user.get_users(*args)
    return json.dump({'error': 'Invalid function'})

def handle_address(function, args):
    return json.dump({'error': 'Invalid function'})

def handle_request(function, args):
    return json.dump({'error': 'Invalid function'})