from django.db import models
 
class UsersModel(models.Model):
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

# class FoodsModel(models.Model):
#     user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
#     food_id = models.IntegerField()

# class RoomsModel(models.Model):
#     room_no = models.IntegerField()
#     room_capacity = models.IntegerField()
#     #daily_status = models.IntegerField() #needs to be updated
#     energy =  models.IntegerField()

# class ParkingsModel(models.Model):
#     user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
#     need_parking = models.IntegerField()
#     date = models.DateField()

# class OfficeBookingsModel(models.Model):
#     user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
#     date = models.DateField()

#class DailyRoomBookings(models.Model):
#    user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
#    room_id = models.ForeignKey(RoomsModel, on_delete=models.CASCADE) #to be found
