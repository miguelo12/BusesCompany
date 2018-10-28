from __future__ import unicode_literals
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet, GenericViewSet
from .models import Choferes, Pasajeros, Buses, Trayectos, AsientoAsignado
from .serializers import choferesCRUDSerializer, pasajerosCRUDSerializer, busesRSerializer, trayectosRSerializer, trayectoCUDSerializer, busCUDSerializer, asientoAsignadoCRUDSerializer # trayectoPasajeroRSerializer
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status

class choferesCRUDViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = choferesCRUDSerializer

    def get_queryset(self):
        return Choferes.objects.all()

class pasajerosCRUDViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = pasajerosCRUDSerializer

    def get_queryset(self):
        return Pasajeros.objects.all()

class busesRViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    lookup_field = 'id'
    serializer_class = busesRSerializer

    def get_queryset(self):
        return Buses.objects.all()

class trayectosRViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    lookup_field = 'id'
    serializer_class = trayectosRSerializer
    
    def get_queryset(self):
        return Trayectos.objects[:1000]

class trayectoCUDViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    lookup_field = 'id'
    serializer_class = trayectoCUDSerializer
    
    def get_queryset(self):
        return Trayectos.objects.all()


class busCUDViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    lookup_field = 'id'
    serializer_class = busCUDSerializer
    
    def get_queryset(self):
        return Buses.objects.all()

class asientoAsignadoCRUDViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = asientoAsignadoCRUDSerializer
    
    def get_queryset(self):
        return Buses.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        asiento = serializer.validated_data
        idBus = request.data.get('id')

        buses_update = Buses.objects(id=idBus)
        if buses_update:
            for k, v in asiento.items():
                for s in v:
                    buses_update.update(push__asientoAsignado=AsientoAsignado(pasajero_id=[*s.items()][1][1],numeroAsiento=[*s.items()][0][1])) #funciona T_T
            return Response()
        
        return Response(status=status.HTTP_404_NOT_FOUND)

# class trayectoPasajeroRViewSet(mixins.RetrieveModelMixin,
#                                mixins.ListModelMixin,GenericViewSet):
#     lookup_field = 'id'
#     serializer_class = trayectoPasajeroRSerializer

#     def list(self, request):
#         return Response(Trayectos.objects)