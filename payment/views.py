from rest_framework import viewsets

from payment.models import PublicCommission, Commission, Invoice, InvoiceFirm
from payment.serializers import PublicCommissionSerializer, CommissionSerializer, InvoiceSerializer, \
    InvoiceFirmSerializer


# Create your views here.
class PublicComissionViewset(viewsets.ModelViewSet):
    queryset = PublicCommission.objects.all()
    serializer_class = PublicCommissionSerializer


class CommissionViewset(viewsets.ModelViewSet):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer


class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceFirmViewset(viewsets.ModelViewSet):
    queryset = InvoiceFirm.objects.all()
    serializer_class = InvoiceFirmSerializer
