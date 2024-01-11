from rest_framework import generics

from .models import Duties
from .serializers import DutiesSerializer


class DutiesAPIView(generics.ListAPIView):
    """Вьюха для выдачи данных по пошлинам."""

    queryset = Duties.objects.select_related(
        'crop',
    ).all()
    serializer_class = DutiesSerializer
