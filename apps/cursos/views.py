from django.shortcuts import render
from rest_framework import viewsets
from .models import Cursos
from .serializers import CursosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializerClass = CursosSerializer
