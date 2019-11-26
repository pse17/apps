import json
from rest_framework import status
from django.urls import reverse
from applications.models import Application
from rest_framework.test import  APITestCase
from django.contrib.auth.models import User

class AppsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        owner = User.objects.create_user('admin', 'admin@admin.com', 'admin')
        Application.objects.create(name='App', key=12345, owner=owner)


    def test_detail(self):
        self.client.login(username='admin', password='admin')
        url = reverse('detail', kwargs={'key': 12345})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data['name'], 'App')


    def test_put(self):
        self.client.login(username='admin', password='admin')
        url = reverse('detail', kwargs={'key': 12345})
        owner = User.objects.get(username='admin')
        response = self.client.put(url, {'name': 'app2'}, format='json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data['name'], 'app2')


    def test_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('add'), {'name': 'App1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'App1')


    def test_list(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)        
