from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

# Local
from .serializers import PersonSerializer
from .models import Persona

class ListaPersonas(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Persona.objects.all()


class PersonaCRUD(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Persona.objects.all()