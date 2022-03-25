# from urllib import response
# from django.contrib.auth.models import User
# from django.urls import reverse

# from django.test import TestCase, Client

# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
# from app.models import Car, Trip

# class UserLogin(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='robert', password='batman')
#         self.car = Car.objects.create(model='Batmobile', speed=300, color="black", doors=4)
#         self.trip = Trip.objects.create(
#             car = self.car,
#             date = '17-03-2022',
#             km = 45
#         )

# class URLTests(TestCase): 
#     def test_homepage(self): 
#         c = Cient()
#         response = self.client.get('/') 
#         self.assertEqual(response.status_code, 200)