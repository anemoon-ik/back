from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Car, Trip, User

class CarsTests(APITestCase):
    def setUp(self):
        user_test = User.objects.create_user(username='test', password='yuy56')
        
        
        self.car = Car.objects.create(user=user_test, model='Tesla', speed=300, color='black', doors=2)

    def test_car_list(self):
        url = f'/cars/{self.car.pk}/trips'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_create(self):
        url = f'/add_car/'
        response = self.client.post(url, {"model": "Batmobile", "speed":200, "color":"black"})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

