from mongoengine import connect, Document, StringField, ListField, ReferenceField

connect(host="mongodb+srv://mydb:bumegalol@matz.2ewqgqh.mongodb.net/?retryWrites=true&w=majority")


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    author = ReferenceField(Author)
    tags = ListField(StringField())
    quote = StringField(required=True)
