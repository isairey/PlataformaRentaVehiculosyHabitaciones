from api.models import Room
from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class RoomsTests(TestCase):

    file_name = 'media/home at beach side.jpg'

    data = {"title": "Room1", "price": 5000, "description": "This is home.", "home_type": "ROOM",
            "room_type": "Single", "total_occupancy": 4, "total_bedrooms": 4,
            "total_bathrooms": 4, "is_furnished": True, "has_kitchen": True,
            "address": "Kathmandu", "image": open(file_name, "rb")}

    def test_home_route_of_rooms(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/rooms/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the content of the response contains messgae.
        self.assertEqual(response.content, b'[]')

    def test_create_and_retrieve_room_data(self):
        user = User.objects.create_renter(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}
        response = self.client.post('/api/v1/rooms/', self.data, **header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'OK')
        self.assertEqual(response.data['data']['title'], self.data['title'])
        self.assertEqual(response.data['data']['price'], self.data['price'])

        data = self.data
        room = Room.objects.create(price=data['price'], title=data['title'],
                                   description=data['description'], home_type=data['home_type'],
                                   room_type=data['room_type'], address=data['address'], owner=user)
        response = self.client.get('/api/v1/rooms/')
        self.assertEqual(response.data[0]['title'], room.title)
        self.assertEqual(response.data[0]['price'], room.price)

        # unique room with title validation test
        # response = self.client.post('/api/v1/rooms/', self.data, **header)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(response.data['title'], ["This field must be unique."])

    def test_retrieve_route_for_room(self):
        data = self.data
        user = User.objects.create_renter(email='normal@user.com', name='normal', password='password@123')
        room = Room.objects.create(price=data['price'], title=data['title'],
                                   description=data['description'], home_type=data['home_type'],
                                   room_type=data['room_type'], address=data['address'], owner=user)

        response = self.client.get(f'/api/v1/rooms/{room.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
