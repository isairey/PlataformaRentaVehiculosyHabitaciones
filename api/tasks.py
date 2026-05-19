import time
from django.db import transaction
from .utils import get_media_url, send_email
from django.contrib.auth import get_user_model
from api.models import Room, Media, Vehicle, Reservation

User = get_user_model()


def create_room(data):
    if User.objects.filter(email=data['user']).exists():
        with transaction.atomic():
            user = User.objects.get(email=data['user'])

            room = Room.objects.create(price=data['price'], title=data['title'], description=data['description'],
                                       home_type=data['home_type'], room_type=data['room_type'],
                                       total_occupancy=data['total_occupancy'], total_bedrooms=data['total_bedrooms'],
                                       total_bathrooms=data['total_bathrooms'], is_furnished=data['is_furnished'],
                                       has_kitchen=data['has_kitchen'], address=data['address'], owner=user)
            media_url = get_media_url(image=data['image'], parent=room)
            Media.objects.create(content_object=room,
                                 file_name=data['image']['file_name'], url=media_url, mime_type='image/png')

            print("Room created successfuly.")
    else:
        print('User Not Found. Data not created')


def create_vehicle(data):
    if User.objects.filter(email=data['user']).exists():
        with transaction.atomic():
            user = User.objects.get(email=data['user'])

            vehicle = Vehicle.objects.create(name=data['name'], price=data['price'], description=data['description'],
                                             capacity=data['capacity'], vehicle_type=data['vehicle_type'],
                                             brand=data['brand'], model=data['model'], owner=user)
            media_url = get_media_url(image=data['image'], parent=vehicle)
            Media.objects.create(content_object=vehicle,
                                 file_name=data['image']['file_name'], url=media_url, mime_type='image/png')

            print("Vehicle created successfuly.")
    else:
        print('User Not Found. Data not created')


def create_reservation(data):
    if User.objects.filter(email=data['user']).exists():
        with transaction.atomic():
            Model = Vehicle if data['service_type'] == 'vehicle' else Room

            user = User.objects.get(email=data['user'])
            service_model = Model.objects.get(pk=data['service_id'])
            Reservation.objects.create(content_object=service_model, start_date=data['start_date'],
                                       price=data['price'], total=data['total'], end_date=data['end_date'], user=user)
            product = {
                "type": 'Vehicle' if data['service_type'] == 'vehicle' else 'Room',
                "id": data['service_id'],
                "date": time.strftime("%a, %d %b %Y %H:%M:%S")
            }
            send_email(sub="Reservation", user=user, owner=service_model.owner, product=product, to=service_model.owner.email)
            print("Reservation created successfuly.")
    else:
        print('User Not Found. Data not created')
