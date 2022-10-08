from schemas.request import Request

def get_requests():
    return Request.objects().to_json()

def add_request(obj):
    request = Request(**obj)
    request.save()
    return request.to_json()

def get_request_by_id(id):
    return Request.objects(id=id).to_json()

def get_requests_by_volunteer_id(id):
    return Request.objects(volunteer=id).to_json()

def get_requests_by_requester_id(id):
    return Request.objects(requester=id).to_json()
