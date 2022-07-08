# import viewsets
from rest_framework import viewsets

from .serializers import UsersSerializer, FoodsSerializer, RoomsSerializer, ParkingsSerializer, OfficeBookingsSerializer
from .models import UsersModel, FoodsModel, RoomsModel, ParkingsModel, OfficeBookingsModel
 
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
