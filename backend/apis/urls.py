from django.urls import include, path

from rest_framework import routers

from apis.views import UsersViewSet, FoodsViewSet, RoomsViewSet, ParkingsViewSet, OfficeBookingsViewSet, DailyRoomBookingsViewSet
#from apis.views1 import DailyRoomBookingsViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'rooms', RoomsViewSet)
router.register(r'parkings', ParkingsViewSet)
router.register(r'foods', FoodsViewSet)
router.register(r'officebookings', OfficeBookingsViewSet)
#router.register(r'allocations', RoomAllocatorViewSet)
router.register(r'allocations',DailyRoomBookingsViewSet)

urlpatterns = [
   path('', include(router.urls)),
]