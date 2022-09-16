from django.db import models

from helpers.models import BaseModel
from staff.models import User
from vebinar.models import Vebinar


# Create your models here.
class Viewer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Review(BaseModel):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    vebinar = models.ForeignKey(Vebinar, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.TextField()
