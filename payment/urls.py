from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('public-commission', PublicComissionViewset, basename='PublicComissionViewset')
router.register('commission', CommissionViewset, basename='CommissionViewset')
router.register('invoice', InvoiceViewset, basename='InvoiceViewset')
router.register('invoice-firm', InvoiceFirmViewset, basename='InvoiceFirmViewset')
