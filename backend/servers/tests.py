from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Server

class ServerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', password='pass')
        self.client.login(username='test', password='pass')

    def test_create_and_list_server(self):
        url = reverse('server-list-create')
        data = {'name': 'Test Server', 'ip': '127.0.0.1'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Server.objects.count(), 1)
        response = self.client.get(url + '?my=1')
        self.assertEqual(len(response.data), 1)