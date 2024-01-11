from django.shortcuts import render
from rest_framework import generics
from .models import Duties
from .serializers import DutiesSerializer


class DutiesAPIView(generics.ListAPIView):
    queryset = Duties.objects.all()
    serializer_class = DutiesSerializer

