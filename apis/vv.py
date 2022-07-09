from datetime import date
from django.views import View

from django.http import JsonResponse

from .serializers import OfficeBookingsSerializer, UsersSerializer, RoomsSerializer, ParkingsSerializer, FoodsSerializer
from .models import OfficeBookingsModel,UsersModel, RoomsModel, ParkingsModel, FoodsModel

def nb_workers_today(request):
    users= OfficeBookingsModel.objects.filter(date=date.today())
    n=len(users)
    return JsonResponse({'number_workers':n})

def total_employees(request):
    users=UsersModel.objects.all()
    n=len(users)
    return JsonResponse({'total_number_workers':n})

def total_rooms(request):
    rooms = RoomsModel.objects.all()
    n=len(rooms)
    return JsonResponse({'number_rooms':n})

#def rooms_today(request):
#    pass

def parking(request):
    parking=ParkingsModel.objects.filter(date=date.today())
    n=len(parking)
    return JsonResponse({'number_parking_slots':n})

def diets_today(request):
    food = FoodsModel.objects.filter(date=date.today())
    no_canteen = len(food.filter(food_type=0))
    meat = len(food.filter(food_type=1))
    vegetarian = len(food.filter(food_type=2))
    vegan = len(food.filter(food_type=3))

    return JsonResponse({'no_food':no_canteen,'meat':meat,'vegetarian':vegetarian,'vegan':vegan})
