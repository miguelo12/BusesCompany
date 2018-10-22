from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from .models import Choferes, Pasajeros, Buses, Trayectos, AsientoAsignado

class ChoferesSerializer(DocumentSerializer):
    class Meta:
        model = Choferes
        fields = '__all__'

class PasajerosSerializer(DocumentSerializer):
    class Meta:
        model = Pasajeros
        fields = '__all__'

class AsientoAsignadoSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = AsientoAsignado
        fields = '__all__'

class BusesSerializer(DocumentSerializer):
    choferes = ChoferesSerializer(many=False)
    asientoAsignado = AsientoAsignadoSerializer(many=True)

    class Meta:
        model = Buses
        fields = '__all__'

class TrayectosSerializer(DocumentSerializer):
    buses = BusesSerializer(many=False)

    class Meta:
        model = Trayectos
        fields = '__all__'