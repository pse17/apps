from django.urls import path
from applications import api

urlpatterns = [
    path('api/list/', api.ApplicationListAPI.as_view(), name='list'),
    path('api/<int:key>', api.ApplicationAPI.as_view(), name='detail'),
    path('api/add', api.ApplicationKeyAPI.as_view(), name='add')
]