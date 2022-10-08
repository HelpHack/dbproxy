import mongoengine

mongoengine.connect('oxylion', host='mongodb://my_user:my_password@hostname:port/my_db?authSource=admin')
