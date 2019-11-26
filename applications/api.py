from random import random
from applications.models import Application
from applications.serializers import ApplicationSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from applications.permissions import IsOwnerOrReadOnly


class ApplicationListAPI(ListAPIView):
    ''' List applications '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationAPI(RetrieveUpdateDestroyAPIView):
    ''' Update and delete application '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = 'key'


class ApplicationKeyAPI(CreateAPIView):
    ''' Create application with random key '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer  

    def perform_create(self, serializer):
        key = round(random() * 100000)
        owner = self.request.user
        return serializer.save(owner=owner, key=key)

    

