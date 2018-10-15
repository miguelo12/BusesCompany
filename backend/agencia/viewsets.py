from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from .models import Choferes, Pasajeros, Buses, Trayectos
from .serializers import ChoferesSerializer, PasajerosSerializer, BusesSerializer, TrayectosSerializer


class ChoferesViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = ChoferesSerializer

    def get_queryset(self):
        return Choferes.objects.all()

class PasajerosViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = PasajerosSerializer

    def get_queryset(self):
        return Pasajeros.objects.all()


class BusesViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = BusesSerializer

    def get_queryset(self):
        return Buses.objects.all()


class TrayectosViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = TrayectosSerializer
    
    def get_queryset(self):
        return Trayectos.objects.all()