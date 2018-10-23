from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet, GenericViewSet
from .models import Choferes, Pasajeros, Buses, Trayectos
from .serializers import ChoferesSerializer, PasajerosSerializer, BusesSerializer, TrayectosSerializer, SetTrayectoSerializer, SetBusSerializer
from rest_framework import mixins

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

class BusesViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    lookup_field = 'id'
    serializer_class = BusesSerializer

    def get_queryset(self):
        return Buses.objects.all()

class TrayectosViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    lookup_field = 'id'
    serializer_class = TrayectosSerializer
    
    def get_queryset(self):
        return Trayectos.objects.all()

class SetTrayectosViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    lookup_field = 'id'
    serializer_class = SetTrayectoSerializer
    
    def get_queryset(self):
        return Trayectos.objects.all()


class SetBusesViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    lookup_field = 'id'
    serializer_class = SetBusSerializer
    
    def get_queryset(self):
        return Buses.objects.all()

