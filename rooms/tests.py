from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import Equipment, Room


def make_room(**kwargs):
    data = dict(name="Room 1", room_type=Room.Type.GROUP, capacity=4,
                hourly_price=Decimal("5.00"), daily_price=Decimal("25.00"))
    data.update(kwargs)
    return Room(**data)


@pytest.mark.django_db
def test_room_is_created_with_equipment():
    room = make_room()
    room.save()
    room.equipment.add(Equipment.objects.create(name="Wi-Fi"))
    assert Room.objects.count() == 1
    assert room.equipment.count() == 1
    assert room.is_active
    assert str(room) == "Room 1 (4p)"


@pytest.mark.django_db
def test_capacity_must_be_greater_than_zero():
    with pytest.raises(ValidationError):
        make_room(capacity=0).full_clean()


@pytest.mark.django_db
def test_max_duration_must_be_greater_than_zero():
    with pytest.raises(ValidationError):
        make_room(max_duration_hours=0).full_clean()


@pytest.mark.django_db
def test_prices_cannot_be_negative():
    with pytest.raises(ValidationError):
        make_room(hourly_price=Decimal("-1.00")).full_clean()


@pytest.mark.django_db
def test_room_name_is_unique():
    make_room().save()
    with pytest.raises(IntegrityError):
        make_room().save()


@pytest.mark.django_db
def test_demo_fixture_loads():
    from django.core.management import call_command
    call_command("loaddata", "demo_rooms", verbosity=0)
    assert Room.objects.filter(is_active=True).count() == 4
