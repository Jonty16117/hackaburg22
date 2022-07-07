# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import ApiSerializer
# from .models import GeeksModel
 
# create a viewset
class ApiViewSet(viewsets.ModelViewSet):
    # define queryset
    # queryset = GeeksModel.objects.all()
     
    # specify serializer to be used
    # serializer_class = GeeksSerializer
    pass