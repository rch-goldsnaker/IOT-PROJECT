from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from .serializers import SensoresSerializer

from .models import sensores

class SensoresViewset(viewsets.ModelViewSet):

    queryset=sensores.objects.all()
    serializer_class=SensoresSerializer