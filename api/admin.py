from django.contrib import admin
from .models import Media, Room, Vehicle, Reservation


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'title', 'price')


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'name', 'price')


class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_id', 'file_name', 'content_type')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'start_date', 'end_date', 'total', 'user', 'content_type')


admin.site.register(Room, RoomAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Reservation, ReservationAdmin)
# Register your models here.
