from api.models import Vehicle
from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class VehiclesTests(TestCase):

    file_name = 'media/car.jpg'

    data = {"name": "Hyundai Konka", "price": 5000, "description": "This is car.", "capacity": 6, "vehicle_type": "Car",
            "brand": "Hyundai", "model": "SUV", "image": open(file_name, "rb")}

    def test_home_route_of_rooms(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/vehicles/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the content of the response contains messgae.
        self.assertEqual(response.content, b'[]')

    def test_create_and_retrieve_vehicle_data(self):
        user = User.objects.create_renter(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}
        response = self.client.post('/api/v1/vehicles/', self.data, **header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'OK')
        self.assertEqual(response.data['data']['name'], self.data['name'])
        self.assertEqual(response.data['data']['price'], self.data['price'])

        data = self.data
        vehicle = Vehicle.objects.create(name=data['name'], price=data['price'], description=data['description'],
                                         capacity=data['capacity'], vehicle_type=data['vehicle_type'],
                                         brand=data['brand'], model=data['model'], owner=user)
        response = self.client.get('/api/v1/vehicles/')
        self.assertEqual(response.data[0]['name'], vehicle.name)
        self.assertEqual(response.data[0]['price'], vehicle.price)

        # Check required fields
        response = self.client.post('/api/v1/vehicles/', **header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_route_for_vehicle(self):
        data = self.data
        user = User.objects.create_renter(email='normal@user.com', name='normal', password='password@123')
        vehicle = Vehicle.objects.create(name=data['name'], price=data['price'], description=data['description'],
                                         capacity=data['capacity'], vehicle_type=data['vehicle_type'],
                                         brand=data['brand'], model=data['model'], owner=user)

        response = self.client.get(f'/api/v1/vehicles/{vehicle.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
