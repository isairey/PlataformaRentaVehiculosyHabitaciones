from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from api.models import Reservation, Room
from django.core.management import call_command

User = get_user_model()


class ReservationsTests(TestCase):

    def test_home_route_of_reservation_without_auth(self):

        # Issue a GET request.
        response = self.client.get('/api/v1/reservations/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_home_route_of_reservation_with_auth(self):
        user = User.objects.create_user(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}
        response = self.client.get('/api/v1/reservations/', **header)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the content of the response contains messgae.
        self.assertEqual(response.content, b'[]')

    def test_create_a_reservation(self):
        user = User.objects.create_user(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}

        call_command('seed', verbosity=3, seed=True)

        # test using room as service
        data = {'service_id': 1, 'service_type': 'room', 'start_date': '2022-02-01', 'end_date': '2022-02-04', 'price': 145, 'total': 1450}
        response = self.client.post('/api/v1/reservations/', data, **header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # test using vehicle as service
        data = {'service_id': 1, 'service_type': 'vehicle', 'start_date': '2022-02-01', 'end_date': '2022-02-04', 'price': 145, 'total': 1450}
        response = self.client.post('/api/v1/reservations/', data, **header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get created reservation
        room = Room.objects.get(pk=1)
        reservation = Reservation.objects.create(content_object=room, start_date=data['start_date'],
                                                 price=data['price'], total=data['total'], end_date=data['end_date'], user=user)

        response = self.client.get('/api/v1/reservations/', **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['reservation_id'], reservation.pk)

    def test_create_a_reservation_without_existing_service(self):
        user = User.objects.create_user(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}

        data = {'service_id': 100, 'service_type': 'room', 'start_date': '2022-02-01', 'end_date': '2022-02-04', 'price': 145, 'total': 1450}
        response = self.client.post('/api/v1/reservations/', data, **header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, b'{"service_id":["Room with id: 100 doesn\'t exists"]}')

    def test_host_reservation_route(self):
        data = {"title": "Room1", "price": 5000, "description": "This is home.", "home_type": "ROOM",
                "room_type": "Single", "total_occupancy": 4, "total_bedrooms": 4,
                "total_bathrooms": 4, "is_furnished": True, "has_kitchen": True,
                "address": "Kathmandu"}
        r_user = User.objects.create_renter(email='normal@user.com', name='normal', password='password@123')
        room = Room.objects.create(price=data['price'], title=data['title'],
                                   description=data['description'], home_type=data['home_type'],
                                   room_type=data['room_type'], address=data['address'], owner=r_user)

        user = User.objects.create_user(email='normalr@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}

        # test using room as service
        data = {'service_id': room.room_id, 'service_type': 'room', 'start_date': '2022-02-01', 'end_date': '2022-02-04', 'price': 145, 'total': 1450}
        response = self.client.post('/api/v1/reservations/', data, **header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_c = self.client.post('/api/v1/token/', {'email': r_user.email, 'password': 'password@123'})
        header_c = {'HTTP_AUTHORIZATION': f'Bearer {response_c.data["access"]}'}

        response = self.client.get('/api/v1/host/reservations/', **header_c)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
