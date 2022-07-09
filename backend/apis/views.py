# import viewsets
from rest_framework import viewsets

from .serializers import UsersSerializer, FoodsSerializer, RoomsSerializer, ParkingsSerializer, OfficeBookingsSerializer, DailyRoomBookingsSerializer
from .models import UsersModel, FoodsModel, RoomsModel, ParkingsModel, OfficeBookingsModel, DailyRoomBookingsModel

from datetime import date
 
class UsersViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = UsersModel.objects.all()
     
    # specify serializer to be used
    serializer_class = UsersSerializer

class FoodsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = FoodsModel.objects.all()
     
    # specify serializer to be used
    serializer_class = FoodsSerializer

class RoomsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = RoomsModel.objects.all()
     
    # specify serializer to be used
    serializer_class = RoomsSerializer

class ParkingsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = ParkingsModel.objects.all()
     
    # specify serializer to be used
    serializer_class = ParkingsSerializer

class OfficeBookingsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = OfficeBookingsModel.objects.all()
     
    # specify serializer to be used
    serializer_class = OfficeBookingsSerializer

class DailyRoomBookingsViewSet(viewsets.ModelViewSet):    
    def optimal_choice(capacities,nb_users):
        return [0,1]

    def room_attr():
        queryset1=list(RoomsModel.objects.all())
        l=[]
        n=[]
        for el in queryset1:
            l.append(el.room_capacity)
            n.append(el.room_name)
        return l,n

    #qs = []
    try:
        q = OfficeBookingsModel.objects.filter(date=date.today())
        nb_users = len(q)
        capacities, names=room_attr()
        room_inds = optimal_choice(capacities,nb_users)
        c=0
        j=0
        print("hello")
        for i in range(nb_users):
            print(q[i].id)
            print(names[room_inds[j]])
            if c<capacities[j]:
                #print("hh")
                c+=1
                #obj = DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
                obj=DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
                #print("hh")
                #qs.append(obj)
            else:
                #print("hh2")
                #obj = DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
                obj=DailyRoomBookingsModel.objects.create(user_id=q[i].id,room_id=names[room_inds[j]])
                #print("hh2")
                #qs.append(obj)
                c=1
                j+=1
    except:
        #print("hh2")
        c=0
        #continue    
        #queryset=qs
    #queryset=None#[]

    queryset = DailyRoomBookingsModel.objects.all()
    #print(r[0].room_capacity)

    serializer_class = DailyRoomBookingsSerializer