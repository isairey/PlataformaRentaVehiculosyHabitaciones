# from django.shortcuts import render
from .producer import publish
from datetime import datetime
from django.db.models import Q
from .utils import write_to_tmp  # , serializeImg
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Room, Vehicle, Reservation
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import RoomSerializer, VehicleSerializer, ReservationSerializer, HostReservationSerializer


class IsAuthenticatedAndRenterOrReadOnly(BasePermission):

    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if (request.method in SAFE_METHODS
            or request.user
                and request.user.is_authenticated and request.user.is_renter):
            return True
        return False


class IsRenter(BasePermission):

    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated
                and request.user.is_renter):
            return True
        return False


class RoomViewSet(viewsets.ViewSet):
    serializer_class = RoomSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [IsAuthenticatedAndRenterOrReadOnly, ]

    def list(self, request):
        queryset = Room.objects.filter(~Q(pk__in=Reservation.objects.filter(active=True, content_type__model='room').values_list('res_room__pk', flat=True))).reverse()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data['image'] = write_to_tmp(file=data['image'])
            data['user'] = request.user.email
            publish(method="create_room", body=data)
            data.pop('image')
            return Response({'message': "OK", 'method': request.method, 'status-code': status.HTTP_201_CREATED,
                            'timestamp': datetime.now(), 'url': request.get_full_path(), 'data': data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Room.objects.filter(pk=pk)
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = RoomSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class VehicleViewSet(viewsets.ViewSet):
    serializer_class = VehicleSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [IsAuthenticatedAndRenterOrReadOnly, ]

    def list(self, request):
        queryset = Vehicle.objects.filter(~Q(pk__in=Reservation.objects.filter(active=True, content_type__model='vehicle').values_list('res_vehicle__pk', flat=True))).reverse()
        serializer = VehicleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data['image'] = write_to_tmp(file=data['image'])
            data['user'] = request.user.email
            publish(method="create_vehicle", body=data)
            # publish(method="save_image", body=str(request.FILES['images'].read()))
            data.pop('image')
            return Response({'message': "OK", 'method': request.method, 'status-code': status.HTTP_201_CREATED,
                            'timestamp': datetime.now(), 'url': request.get_full_path(), 'data': data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Vehicle.objects.filter(pk=pk)
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = VehicleSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationSerializer

    def list(self, request):
        queryset = Reservation.objects.filter(user=request.user).reverse()
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data['user'] = request.user.email
            publish(method="create_reservation", body=data)
            return Response({'message': "OK", 'method': request.method, 'status-code': status.HTTP_201_CREATED,
                            'timestamp': datetime.now(), 'url': request.get_full_path(), 'data': data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicesViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsRenter]

    def list(self, request):
        queryset_room = Room.objects.filter(owner=request.user).reverse()
        serializer_room = RoomSerializer(queryset_room, many=True)
        queryset_vehicle = Vehicle.objects.filter(owner=request.user)
        serializer_vehicle = VehicleSerializer(queryset_vehicle, many=True)
        return Response({'message': "OK", 'method': request.method, 'status-code': status.HTTP_200_OK,
                         'timestamp': datetime.now(), 'url': request.get_full_path(),
                         'rooms': serializer_room.data, 'vehicles': serializer_vehicle.data})


class HostReservationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsRenter]

    def list(self, request):
        queryset_room = Reservation.objects.filter(res_room__owner=request.user).reverse()
        serializer_room = HostReservationSerializer(queryset_room, many=True)
        queryset_vehicle = Reservation.objects.filter(res_vehicle__owner=request.user).reverse()
        serializer_vehicle = HostReservationSerializer(queryset_vehicle, many=True)
        return Response({'message': "OK", 'method': request.method, 'status-code': status.HTTP_200_OK,
                         'timestamp': datetime.now(), 'url': request.get_full_path(),
                         'rooms': serializer_room.data, 'vehicles': serializer_vehicle.data})
