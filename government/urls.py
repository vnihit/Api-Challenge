from django.urls import path
from .views import *

urlpatterns = [
    path("company/<int:index>/", get_all_persons),
    path("common_friends/<int:index_1>/other/<int:index_2>/", common_friends),
    path("food_choice/<int:index>/",food_choice)
]