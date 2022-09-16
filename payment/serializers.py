from rest_framework import serializers

from payment.models import PublicCommission, Commission, Invoice, InvoiceFirm


class PublicCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicCommission
        fields = '__all__'


class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceFirm
        fields = '__all__'
