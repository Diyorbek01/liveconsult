from django.db import models

from helpers.models import BaseModel
from staff.models import Firm, User
from vebinar.models import Vebinar, Subscription
from viewer.models import Viewer


# Create your models here.
class PublicCommission(BaseModel):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class PrivateCommission(BaseModel):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    is_active = models.BooleanField(default=True)


class Commission(BaseModel):
    base_commission = models.ForeignKey(PublicCommission, on_delete=models.CASCADE)
    min_sum = models.PositiveBigIntegerField()
    max_sum = models.PositiveBigIntegerField()
    percent = models.IntegerField()


class Invoice(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    card = models.PositiveBigIntegerField()
    expire_date = models.CharField(max_length=5)


class InvoiceFirm(BaseModel):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    vebinar = models.ForeignKey(Vebinar, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField(Subscription, blank=True)
    total_amount = models.PositiveBigIntegerField()
    is_payment_transfered = models.BooleanField(default=False)
    is_requested = models.BooleanField(default=False)
    date_of_payment_orginazer_recieved = models.DateTimeField(null=True, blank=True)
    date_of_payment_ITF_recieved = models.DateTimeField(null=True, blank=True)
