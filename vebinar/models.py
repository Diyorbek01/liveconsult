from django.db import models

from category.models import Category
from helpers.models import BaseModel
from staff.models import Expert, Firm, User


# Create your models here.
class Vebinar(BaseModel):
    STATUS = (
        ("appear", "appear"),
        ("cancel", "cancel"),
        ("delete", "delete"),
    )
    orginazer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    experts = models.ManyToManyField(Expert)
    price = models.PositiveBigIntegerField()
    duration = models.IntegerField()
    number_of_viewers = models.PositiveIntegerField()
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS, default="appear")


class Scheduler(BaseModel):

    vebinar = models.ForeignKey(Vebinar, on_delete=models.CASCADE)
    date = models.DateTimeField()
    is_organized = models.BooleanField(default=True)



class Subscription(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vebinar = models.ForeignKey(Vebinar, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    fee = models.PositiveBigIntegerField()
    amount_organizer_recieves = models.PositiveBigIntegerField()
    commission_ITF_receives = models.PositiveBigIntegerField()
