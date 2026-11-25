from django.contrib import admin

from .models import Equipment, Room


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "room_type", "capacity", "hourly_price", "daily_price", "is_active")
    list_filter = ("room_type", "is_active", "equipment")
    search_fields = ("name",)
    filter_horizontal = ("equipment",)
