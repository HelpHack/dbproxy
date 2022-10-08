import json
from . import user, address, request

def handle_user(function, args):
    if function == 'get_users':
        return user.get_users(*args)
    if function == 'add_user':
        return user.add_user(*args)
    if function == 'get_user_by_id':
        return user.get_user_by_id(*args)
    return json.dump({'error': 'Invalid function'})

def handle_address(function, args):
    if function == 'get_addresses':
        return address.get_addresses(*args)
    if function == 'add_address':
        return address.add_address(*args)
    if function == 'get_address_by_id':
        return address.get_address_by_id(*args)
    if function == 'get_addresses_by_user_id':
        return address.get_addresses_by_user_id(*args)
    return json.dump({'error': 'Invalid function'})

def handle_request(function, args):
    if function == 'get_requests':
        return request.get_requests(*args)
    if function == 'add_request':
        return request.add_request(*args)
    if function == 'get_request_by_id':
        return request.get_request_by_id(*args)
    if function == 'get_requests_by_volunteer_id':
        return request.get_requests_by_volunteer_id(*args)
    if function == 'get_requests_by_requester_id':
        return request.get_requests_by_requester_id(*args)
    return json.dump({'error': 'Invalid function'})