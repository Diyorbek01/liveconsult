from django.db import models

from helpers.models import BaseModel


# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=100)

class Profession(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Skill(BaseModel):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)