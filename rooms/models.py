from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "equipment"

    def __str__(self):
        return self.name


class Room(models.Model):
    class Type(models.TextChoices):
        INDIVIDUAL = "individual", "Individual"
        GROUP = "group", "Group"
        MEETING = "meeting", "Meeting"
        TRAINING = "training", "Training"

    name = models.CharField(max_length=50, unique=True)
    room_type = models.CharField(max_length=20, choices=Type.choices)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    equipment = models.ManyToManyField(Equipment, blank=True, related_name="rooms")
    max_duration_hours = models.PositiveIntegerField(default=4, validators=[MinValueValidator(1)])
    buffer_minutes = models.PositiveIntegerField(default=15)
    hourly_price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    daily_price = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.capacity}p)"
