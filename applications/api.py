from django.http import Http404
from applications.models import Application
from applications.serializers import ApplicationSerializer, ApplicationKeySerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from applications.permissions import IsOwnerOrReadOnly


class ApplicationListAPI(APIView):
    ''' List application '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        app = Application.objects.all()
        serializer = ApplicationSerializer(app, many=True)
        return Response(serializer.data)


class ApplicationAPI(APIView):
    ''' Update and delete application '''

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, key):
        try:
            return Application.objects.get(key=key)
        except Application.DoesNotExist:
            raise Http404
    
    def get(self, request, key, format=None):
        app = self.get_object(key)
        serializer = ApplicationSerializer(app)
        return Response(serializer.data)

    def put(self, request, key, format=None):
        app = self.get_object(key)
        serializer = ApplicationSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, key, format=None):
        app = self.get_object(key)
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationKeyAPI(APIView):
    ''' Create application with key '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = ApplicationKeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, key=42)
