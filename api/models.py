from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

User = get_user_model()


class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    url = models.URLField(max_length=255)
    mime_type = models.CharField(max_length=100, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, related_name='medias', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.media_id)


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.IntegerField()
    total = models.IntegerField()
    active = models.BooleanField(default=True)

    # status
    content_type = models.ForeignKey(ContentType, related_name='reservations', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.reservation_id)


class Room(models.Model):
    # home_types = (
    #     ("R", "ROOM"),
    #     ("F", "FLAT"),
    #     ("A", "APPARTMENT"),
    #     ("H", "HOUSE")
    # )
    # room_types = (
    #     ("S", "Single"),
    #     ("D", "Double"),
    #     ("T", "Triple"),
    #     ("Q", "Queen"),
    #     ("K", "King"),
    # )
    room_id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, default='')

    home_type = models.CharField(max_length=100)  # ,choices=home_types)
    room_type = models.CharField(max_length=100)  # ,choices=room_types)

    total_occupancy = models.IntegerField(null=True, blank=True)
    total_bedrooms = models.IntegerField(null=True, blank=True)
    total_bathrooms = models.IntegerField(null=True, blank=True)
    is_furnished = models.BooleanField(null=True, blank=True)
    has_kitchen = models.BooleanField(null=True, blank=True)
    has_internet = models.BooleanField(null=True, blank=True)
    has_parking = models.BooleanField(null=True, blank=True)
    has_garden = models.BooleanField(null=True, blank=True)
    has_terrace = models.BooleanField(null=True, blank=True)
    min_stay = models.IntegerField(null=True, blank=True)
    max_stay = models.IntegerField(null=True, blank=True)
    floor_no = models.IntegerField(null=True, blank=True)

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    images = GenericRelation(Media)
    reservations = GenericRelation(Reservation, related_query_name="res_room")
    owner = models.ForeignKey(User, related_name='rooms', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.room_id)


class Vehicle(models.Model):

    # vehicle_types = (
    #     ("B", "Bike"),
    #     ("C", "Car"),
    #     ("P", "Pickup"),
    # )

    vehicle_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=500, blank=True, default='')

    capacity = models.IntegerField()
    vehicle_type = models.CharField(max_length=100)  # , choices=vehicle_types)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    plate_number = models.CharField(max_length=100, null=True, blank=True)

    images = GenericRelation(Media)
    reservations = GenericRelation(Reservation, related_query_name="res_vehicle")
    owner = models.ForeignKey(User, related_name='vehicles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.vehicle_id)
