# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import UsersModel, FoodsModel, RoomsModel, ParkingsModel, OfficeBookingsModel, TotalUsersModel
 
# Create a model serializer
class UsersSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = UsersModel
        fields = ['id','username', 'email','password']

class FoodsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = FoodsModel
        fields = ('id','user_id', 'food_type', 'date')

class RoomsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = RoomsModel
        fields = ('id', 'room_no','room_capacity','energy')

class ParkingsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = ParkingsModel
        fields = ('id','user_id','need_parking','date')

class OfficeBookingsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = OfficeBookingsModel
        fields = ('id','user_id', 'date')

class TotalUsersSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = TotalUsersModel
        fields = ('id','number')