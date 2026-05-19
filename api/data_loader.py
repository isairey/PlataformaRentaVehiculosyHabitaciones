import json
from tqdm import tqdm
from faker import Faker
from api.models import Room, Vehicle, Media
# from multiprocessing import Pool, cpu_count
from django.contrib.auth import get_user_model

fake = Faker()
User = get_user_model()


def seed_admin_and_test_user():
    """Seed Dummy User to the database

    Args:
        count (int, optional): [Number of user to seed]. Defaults to 10.
    """

    if User.objects.filter(email='test@email.com').exists() and User.objects.filter(email='admin@admin.com').exists():
        print("Test and Admin User already exists.")
    else:
        print("Creating a Test and Admin User")
        User.objects.create_user(email='test@email.com', name='testuser', password='password')
        User.objects.create_superuser(email='admin@admin.com', name='Admin user', password='admin')
        # user = User.objects.create_renter(email='normal@user.com', name='normal', password='password@123')


def seed_users(count: int = 30):
    """Seed Dummy User to the database

    Args:
        count (int, optional): [Number of user to seed]. Defaults to 10.
    """
    for _ in tqdm(range(count), desc="Seeding User Data :"):
        User.objects.create_user(email=fake.email(), name=fake.name(), password=fake.password())


def create_room(data):
    user = User.objects.filter(pk=fake.random_int(1, 30))
    if user.exists():
        images = data.pop('images')
        room = Room.objects.create(**data, owner=user.get())
        for image in images:
            Media.objects.create(content_object=room,
                                 file_name=image['name'], url=image['url'], mime_type='image/png')


def seed_rooms():
    with open('datas/rooms.json', 'r') as f:
        datas = json.load(f)
    if datas:
        for data in tqdm(datas):
            create_room(data)

        # with Pool(processes=cpu_count()) as pool:
        #     pool.map(create_room, tqdm(datas, desc="Seeding Rooms Data :"))


def create_vehicle(data):
    user = User.objects.filter(pk=fake.random_int(1, 30))
    if user.exists():
        images = data.pop('images')
        vehicle = Vehicle.objects.create(**data, owner=user.get())
        for image in images:
            Media.objects.create(content_object=vehicle,
                                 file_name=image['name'], url=image['url'], mime_type='image/png')


def seed_vehicles():
    with open('datas/vehicles.json', 'r') as f:
        datas = json.load(f)
    if datas:
        for data in tqdm(datas):
            create_vehicle(data)
        # with Pool(processes=cpu_count()) as pool:
        #     pool.map(create_vehicle, tqdm(datas, desc="Seeding Vehicle Data :"))
