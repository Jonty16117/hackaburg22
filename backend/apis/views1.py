# import viewsets
from rest_framework import viewsets

from .serializers import UsersSerializer, FoodsSerializer, RoomsSerializer, ParkingsSerializer, OfficeBookingsSerializer, DailyRoomBookingsSerializer
from .models import UsersModel, FoodsModel, RoomsModel, ParkingsModel, OfficeBookingsModel, DailyRoomBookingsModel

from datetime import date

#constrain to only get request
class DailyRoomBookingsViewSet(viewsets.ModelViewSet):    
    def optimal_choice():
        return [2,4]

    def room_attr():
        queryset1=list(RoomsModel.objects.all())
        l=[]
        n=[]
        for el in queryset1:
            l.append(el.room_cap)
            n.append(el.room_name)
        return l,n
    
    q = OfficeBookingsModel.objects.filter(date=date.today())
    #print(type(q))
    nb_users = len(q)
    capacities, names=room_attr()
    room_inds = optimal_choice(capacities,nb_users)

    qs = []
    c=0
    j=0
    for i in range(nb_users):
        if c<capacities[j]:
            c+=1
            #obj = DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
            DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
            #qs.append(obj)
        else:
            #obj = DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
            DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
            #qs.append(obj)
            c=1
            j+=1
        
        #queryset=qs
        #queryset=None#[]

    #queryset = OfficeBookingsModel.objects.filter(date=date.today())
    #print(r[0].room_capacity)

    #serializer_class = DailyRoomBookingsSerializer