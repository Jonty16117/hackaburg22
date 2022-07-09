from datetime import date
from django.views import View

from django.http import JsonResponse

from .serializers import OfficeBookingsSerializer, UsersSerializer, RoomsSerializer, ParkingsSerializer, FoodsSerializer
from .models import OfficeBookingsModel,UsersModel, RoomsModel, ParkingsModel, FoodsModel

import numpy as np

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

def room_attr():
    queryset1=list(RoomsModel.objects.all())
    l=[]
    n=[]
    e=[]
    for el in queryset1:
        l.append(el.room_capacity)
        n.append(el.room_no)
        e.append(el.energy)
    return l,e,n

def optimal_choice(capacities,nb_users):
    k=np.argsort(capacities)
    k1=np.sort(capacities)
    s=0
    room_inds=[]
    for i in range(k.shape[0]):
        if s<nb_users:
            s+=k1[i]
            room_inds.append(k[i])
        else:
            break
    return room_inds

def allocate_rooms(request):
    q = OfficeBookingsModel.objects.filter(date=date.today())
    nb_users=len(q)
    capacities, e, names=room_attr()
    room_inds = optimal_choice(capacities,nb_users)
    print(names)
    qs = dict()
    c=0
    j=0
    for i in range(nb_users):
        if c<capacities[j]:
            c+=1            
        else:
            print("hi")
            c=1
            j+=1
        qs[str(q[i].user_id)]=names[room_inds[j]]
    
    return JsonResponse(qs)

def rooms_today(request):
    q = OfficeBookingsModel.objects.filter(date=date.today())
    nb_users=len(q)
    capacities, names=room_attr()
    room_inds = optimal_choice(capacities,nb_users)
    qs = dict()
    qs["room_names"]=[]

    for i in range(room_inds):
        qs["room_names"].append(names[i])
    
    return JsonResponse(qs)

def energy_used_today(request):
    q = OfficeBookingsModel.objects.filter(date=date.today())
    nb_users=len(q)
    capacities, e,names=room_attr()
    room_inds = optimal_choice(capacities,nb_users)
    qs = dict()
    qs["energy_today"]=0

    for i in range(room_inds):
        qs["room_names"]=e[room_inds[j]]
    
    return JsonResponse(qs)