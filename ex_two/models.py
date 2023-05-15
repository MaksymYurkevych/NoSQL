from mongoengine import connect, Document, StringField, BooleanField

connect(host="mongodb+srv://mydb:bumegalol@matz.2ewqgqh.mongodb.net/?retryWrites=true&w=majority")


class Client(Document):
    fullname = StringField(required=True)
    email = StringField()
    phone = StringField()
    address = StringField()
    sent_message = BooleanField()
    best_method = StringField()