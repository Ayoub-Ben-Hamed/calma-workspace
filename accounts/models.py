from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Étudiant"
        PUPIL = "pupil", "Élève du secondaire"
        DEVELOPER = "developer", "Développeur"
        ENTREPRENEUR = "entrepreneur", "Entrepreneur"
        MANAGER = "manager", "Gérant"
        FRONT_DESK = "front_desk", "Agent de suivi"
        CASHIER = "cashier", "Agent de paiement"
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    phone = models.CharField(max_length=20, blank=True)
