from mongoengine import Document ,fields,connect
connect('mongotask')

class User(Document):
    email = fields.StringField(max_length=100)
    username = fields.StringField(max_length=50)
    password = fields.StringField(max_length = 100)

