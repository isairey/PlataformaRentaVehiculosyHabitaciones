import factory
from faker import Faker
from django.contrib.auth import get_user_model
from api.models import Room, Vehicle, Media
fake = Faker()
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = fake.name()
    # email = fake.word().lower()+''.join(name.lower().split())+'@email.com'
    email = fake.word().lower()+fake.email()
    password = fake.password()


vehicle_types = (
    ("B", "Bike"),
    ("C", "Car"),
    ("P", "Pickup"),
)
home_types = (
    ("R", "ROOM"),
    ("F", "FLAT"),
    ("A", "APPARTMENT"),
    ("H", "HOUSE")
)
room_types = (
    ("S", "Single"),
    ("D", "Double"),
    ("T", "Triple"),
    ("Q", "Queen"),
    ("K", "King"),
)
# owner = UserFactory()


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    title = fake.sentence(fake.random_int(3, 6))
    price = fake.random_int(1000, 5000)
    description = fake.sentence(fake.random_int(40, 80))

    home_type = home_types[fake.random_int(0, 3)][0]
    room_type = room_types[fake.random_int(0, 4)][0]

    total_occupancy = fake.random_int(2, 8)
    total_bedrooms = fake.random_int(2, 5)
    total_bathrooms = fake.random_int(1, 3)
    is_furnished = fake.random_int(0, 1)
    has_kitchen = fake.random_int(0, 1)
    has_internet = fake.random_int(0, 1)
    has_parking = fake.random_int(0, 1)
    has_garden = fake.random_int(0, 1)
    has_terrace = fake.random_int(0, 1)
    min_stay = fake.random_int(1, 5)
    max_stay = fake.random_int(10, 30)
    floor_no = fake.random_int(1, 5)

    address = fake.address()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()
    latitude = fake.latitude()
    longitude = fake.longitude()

    owner = factory.SubFactory(UserFactory)


class VehicleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vehicle

    name = fake.sentence(fake.random_int(3, 6))
    price = fake.random_int(1000, 5000)
    description = fake.sentence(fake.random_int(40, 80))

    capacity = fake.random_int(2, 10)
    vehicle_type = vehicle_types[fake.random_int(0, 2)][0]
    brand = fake.company()
    model = fake.sentence(fake.random_int(2, 5))
    plate_number = fake.license_plate()

    owner = factory.SubFactory(UserFactory)


class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Media

    file_name = fake.sentence(fake.random_int(3, 6))
    url = fake.url()
    mime_type = 'image/jpg'
    content_object = factory.SubFactory(VehicleFactory)


def seed_data(num=1):
    try:
        user = UserFactory.create()
        vehicle = VehicleFactory.create(owner=user)
        MediaFactory(content_object=vehicle)
        MediaFactory(content_object=vehicle)
        print(f"Vehicle with name : {vehicle.name} created.")

        room = RoomFactory.create(owner=user)
        MediaFactory(content_object=room)
        MediaFactory(content_object=room)
        print(f"Room with name : {room.title} created.")
    except Exception as E:
        print("An exception occurred", E)
