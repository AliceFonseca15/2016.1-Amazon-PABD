from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet:

queryset = Cliente.objects.all()
serializer_class = ClienteSerializer