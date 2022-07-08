# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers
 
# import everything from views
from .views import *
 
# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register('user_list/',listusers.as_view())
#router.register(r'^users/$', UsersViewSet)
#router.register(r'foods', FoodsViewSet)
#router.register(r'rooms', RoomsViewSet)
#router.register(r'parkings', ParkingsViewSet)
#router.register(r'officebookings', OfficeBookingsViewSet)
 
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]