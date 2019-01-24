from django.db import models
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *
# Create your models here.


class Company(Document):
    meta = {'collection': 'Company'}

    index = IntField(required=True)
    company = StringField(required=True)


class Friends(EmbeddedDocument):
    index = IntField(required=True)

class Person(Document):

    index = IntField(required=True)
    has_died = BooleanField(required=True)
    eyeColor = StringField(required=True)
    name = StringField(required=True)
    company_id = IntField(required=True)
    age = IntField()
    guid = StringField()
    address = StringField()
    phone = StringField()
    favouriteFood = ListField(StringField())
    tags = ListField(StringField())
    friends = EmbeddedDocumentListField(Friends)
    registered = StringField()
    greeting = StringField()
    email = EmailField()
    about = StringField()
    gender = StringField(choices=['male', 'female'])
    balance = StringField()
    picture = URLField()

    meta = {'collection': 'People'}

class FoodCategory(Document):

    item = StringField(required=True)
    category = StringField(required=True, choices=['fruit', 'vegetable'])

    meta = {'collection': 'FoodCategory'}
