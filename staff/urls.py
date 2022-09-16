from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('firm', FirmViewset, basename='FirmViewset')
router.register('expert', ExpertViewset, basename='ExpertViewset')
