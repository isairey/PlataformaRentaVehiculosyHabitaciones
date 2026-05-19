from .models import Media, Room, Vehicle, Reservation
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
from accounts.serializers import BasicUserSerializer


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'media_id',
            'file_name',
            'url',
            'mime_type',
        )
        extra_kwargs = {'media_id': {'read_only': True}}


class MediaObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `content_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize.
        """
        serializer = MediaSerializer(value)

        return serializer.data


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=255)  # , validators=[UniqueValidator(queryset=Room.objects.all())])
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=500)
    home_type = serializers.CharField()
    room_type = serializers.CharField()
    total_occupancy = serializers.IntegerField()
    total_bedrooms = serializers.IntegerField()
    total_bathrooms = serializers.IntegerField()
    is_furnished = serializers.BooleanField()
    has_kitchen = serializers.BooleanField()
    address = serializers.CharField()
    image = serializers.ImageField(max_length=None, write_only=True)

    images = MediaObjectRelatedField(read_only=True, many=True)
    owner = BasicUserSerializer(read_only=True)

    class Meta:
        depth = 1
        model = Room
        fields = (
            'room_id',
            'title',
            'price',
            'description',
            'home_type',
            'room_type',
            'total_occupancy',
            'total_bedrooms',
            'total_bathrooms',
            'is_furnished',
            'has_kitchen',
            'address',
            'images',
            'owner',
            'image'
        )
        read_only_fields = ('room_id', 'images', 'owner')


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=500)
    capacity = serializers.IntegerField()
    vehicle_type = serializers.CharField()
    brand = serializers.CharField()
    model = serializers.CharField()
    image = serializers.ImageField(max_length=None, write_only=True)

    images = MediaObjectRelatedField(read_only=True, many=True)
    owner = BasicUserSerializer(read_only=True)

    class Meta:
        depth = 1
        model = Vehicle
        fields = (
            'vehicle_id',
            'name',
            'price',
            'description',
            'capacity',
            'vehicle_type',
            'brand',
            'model',
            'images',
            'owner',
            'image'
        )
        read_only_fields = ('vehicle_id', 'images', 'owner')


class ReservationObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `tagged_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize bookmark instances using a bookmark serializer,
        and note instances using a note serializer.
        """
        if isinstance(value, Room):
            serializer = RoomSerializer(value)
        elif isinstance(value, Vehicle):
            serializer = VehicleSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data


class ReservationSerializer(serializers.ModelSerializer):
    service_id = serializers.IntegerField(write_only=True)
    service_type = serializers.ChoiceField(choices=['vehicle', 'room'], write_only=True)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    price = serializers.IntegerField()
    total = serializers.IntegerField()

    content_object = ReservationObjectRelatedField(read_only=True)

    class Meta:
        depth = 1
        model = Reservation
        fields = (
            'reservation_id',
            'service_id',
            'service_type',
            'start_date',
            'end_date',
            'price',
            'total',
            'content_object',
            'content_type'
        )
        extra_kwargs = {'reservation_id': {'read_only': True}, 'content_type': {'read_only': True}}

    def validate(self, data):
        """
        Custom Validations
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"end_date": "finish must occur after start"})

        Model = Vehicle if data['service_type'] == 'vehicle' else Room
        if not Model.objects.filter(pk=data['service_id']).exists():
            raise serializers.ValidationError({"service_id": f"{Model._meta.model.__name__} with id: {data['service_id']} doesn't exists"})
        return data


class HostReservationSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(read_only=True)
    end_date = serializers.DateTimeField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    total = serializers.IntegerField(read_only=True)

    user = BasicUserSerializer(read_only=True)
    content_object = ReservationObjectRelatedField(read_only=True)

    class Meta:
        depth = 1
        model = Reservation
        fields = (
            'reservation_id',
            'start_date',
            'end_date',
            'price',
            'total',
            'user',
            'content_object',
            'content_type'
        )
        extra_kwargs = {'reservation_id': {'read_only': True}, 'content_type': {'read_only': True}}
