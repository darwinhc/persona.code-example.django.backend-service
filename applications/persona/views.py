from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

# Local
from .serializers import PersonSerializer
from .models import Persona

class PersonaCRUD(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Persona.objects.all()