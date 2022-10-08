from schemas.address import Address

def get_addresses():
    return Address.objects().to_json()

def add_address(obj):
    address = Address(**obj)
    address.save()
    return address.to_json()

def get_address_by_id(id):
    return Address.objects(id=id).to_json()

def get_addresses_by_user_id(id):
    return Address.objects(user=id).to_json()