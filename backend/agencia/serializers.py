from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from .models import Choferes, Pasajeros, Buses, Trayectos, AsientoAsignado

class choferesCRUDSerializer(DocumentSerializer):
    class Meta:
        model = Choferes
        fields = '__all__'

class pasajerosCRUDSerializer(DocumentSerializer):
    class Meta:
        model = Pasajeros
        fields = '__all__'

class AsientoAsignadoSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = AsientoAsignado
        fields = '__all__'

class busesRSerializer(DocumentSerializer):
    choferes = choferesCRUDSerializer(many=False)
    asientoAsignado = AsientoAsignadoSerializer(many=True)

    class Meta:
        model = Buses
        fields = '__all__'

class trayectosRSerializer(DocumentSerializer):
    buses = busesRSerializer(many=False)

    class Meta:
        model = Trayectos
        fields = '__all__'




class trayectoCUDSerializer(DocumentSerializer):
    class Meta:
        model = Trayectos
        fields = '__all__'

class busCUDSerializer(DocumentSerializer):
    class Meta:
        model = Buses
        fields = '__all__'

class asientoAsignadoCRUDSerializer(DocumentSerializer):
    asientoAsignado = AsientoAsignadoSerializer(many=True)

    class Meta:
        model = Buses
        fields = ['id','asientoAsignado']

class trayectoPasajeroRSerializer(DocumentSerializer):
    buses = busesRSerializer(many=False)
    class Meta:
        model = Trayectos
        fields = '__all__'
