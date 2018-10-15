from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from .models import Choferes, Pasajeros, Buses, Trayectos, AsientoAsignado

class ChoferesSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Choferes
        fields = '__all__'

class PasajerosSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Pasajeros
        fields = '__all__'

class AsientoAsignadoSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = AsientoAsignado
        fields = '__all__'

class BusesSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Buses
        fields = '__all__'

class TrayectosSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Trayectos
        fields = '__all__'