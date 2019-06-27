from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from deliverers.models import Deliverer


class DelivererListResource(viewsets.ModelViewSet):
    queryset = Deliverer.objects.all()
    permission_classes = [AllowAny]
