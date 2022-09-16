from django.contrib.auth.models import AbstractUser
from django.db import models

from helpers.models import BaseModel


# Create your models here.
class User(AbstractUser):
    ROLE = (
        ("firm", "firm"),
        ("expert", "expert"),
        ("viewer", "viewer"),
    )
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20)
    balance = models.BigIntegerField(default=0)


class Firm(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Expert(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
