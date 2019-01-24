from rest_framework_mongoengine import serializers
from .models import *

class PeopleSerializer(serializers.DocumentSerializer):
    
    class Meta:
        model = Person
        fields = "__all__"
        depth = 1