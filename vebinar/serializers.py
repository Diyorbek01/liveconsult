from rest_framework import serializers

from vebinar.models import Vebinar, Scheduler, Subscription


class VebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vebinar
        fields = '__all__'


class SchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
