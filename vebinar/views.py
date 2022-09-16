from rest_framework import viewsets

from vebinar.models import Vebinar, Scheduler, Subscription
from vebinar.serializers import VebinarSerializer, SchedulerSerializer, SubscriptionSerializer


# Create your views here.
class VebinarViewset(viewsets.ModelViewSet):
    queryset = Vebinar.objects.all()
    serializer_class = VebinarSerializer


class SchedulerViewset(viewsets.ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer


class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
