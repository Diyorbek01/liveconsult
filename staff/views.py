from rest_framework import viewsets

from staff.models import Firm, Expert
from staff.serializers import FirmSerializer, ExpertSerializer


# Create your views here.
class FirmViewset(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class ExpertViewset(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
