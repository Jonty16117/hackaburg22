from django.urls import include, path

from rest_framework import routers

from apis.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
# router.register(r'species', SpeciesViewSet)

urlpatterns = [
   path('', include(router.urls)),
]