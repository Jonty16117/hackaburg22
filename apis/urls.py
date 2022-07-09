from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from apis.views import UsersViewSet, FoodsViewSet, RoomsViewSet, ParkingsViewSet, OfficeBookingsViewSet#, TotalUsersViewSet
from apis.vv import *

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'rooms', RoomsViewSet)
router.register(r'parkings', ParkingsViewSet)
router.register(r'foods', FoodsViewSet)
router.register(r'officebookings', OfficeBookingsViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('nb_workers_today/', nb_workers_today),
   path('total_employees/', total_employees),
   path('total_rooms/', total_rooms),
   path('parking/', parking),
   path('diets_today/', diets_today),
   path('allocate_rooms/',allocate_rooms),
   path('rooms_today/',rooms_today),
]
#urlpatterns = format_suffix_patterns(urlpatterns)