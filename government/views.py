from .models import Company, Person, FoodCategory
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def get_all_persons(request, index):
    """All persons working for a company"""
    persons = Person.objects(company_id=index)
    if not persons:
        return Response({"message": "No people work in this company"}, status=status.HTTP_404_NOT_FOUND)
    serializer = PeopleSerializer(persons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def common_friends(request, index_1, index_2):
    """Common friends who are still alive with eyeColor=brown """
    person_1 = Person.objects(index=index_1).first()
    if not person_1:
        return Response({"message": "First person not found"}, status=status.HTTP_404_NOT_FOUND)
    
    #
    person_2 = Person.objects(index=index_2).first()
    if not person_2:
        return Response({"message": "Index of the second person is missing"}, status=status.HTTP_400_BAD_REQUEST)
    
    # select index of friends not including the person himself
    person_1_friends_indices = [friend_object.index for friend_object in person_1.friends if friend_object.index!=person_1.index]
    person_2_friends_indices = [friend_object.index for friend_object in person_2.friends if friend_object.index!=person_2.index]

    # fidn intersection 
    all_common_friends = list(filter(lambda x: x in person_1_friends_indices, person_2_friends_indices))

    # filter according to the given criteria
    friends = Person.objects(index__in=all_common_friends, eyeColor='brown',has_died=False)
    if not friends:
        return Response({"message": "No friends with matching criteria found"})
    serializer = PeopleSerializer(friends, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def food_choice(request, index):
    """Favourite food of a person. food items are categorized as fruits and vegetables"""
    person = Person.objects(index=index).first()
    if not person:
        return Response({"message": "Person with index not found"}, status=status.HTTP_404_NOT_FOUND)
    
    fruits = FoodCategory.objects(item__in=person.favouriteFood, category="fruit")
    vegetables = FoodCategory.objects(item__in=person.favouriteFood, category="vegetable")

    result = {
        "username": person.name,
        "age": person.age,
        "fruits":[x.item for x in fruits],
        "vegetables":[x.item for x in vegetables]
    }
    return Response(result, status=status.HTTP_200_OK)