import json
from logging import Logger
import routes

def invoke_function(route, args):
    if not route.find('/'):
        Logger.error('')
        return json.dumps({'error': 'Missing route <route>/...'})
    [namespace, function] = route.split('/')
    if namespace == 'user':
        return routes.handle_user(function, args)
    elif namespace == 'address':
        return routes.handle_address(function, args)
    elif namespace == 'request':
        return routes.handle_request(function, args)
    Logger.error('Invalid route')
    return json.dumps({'error': 'Invalid route'})

def handle_request(body):
    try:
        data = json.loads(body)
        if not ('route' in data):
            Logger.error('No \'route\' property found')
            return json.dumps({'error': 'No \'route\' property found'})
        if not ('arguments' in data):
            Logger.error('No \'arguments\' property found')
            return json.dumps({'error': 'No \'arguments\' property found'})
        return invoke_function(data['route'], data['arguments'])
    except Exception as e:
        return json.dumps({'error': str(e)})