from rest_framework import routers
from agencia.viewsets import ChoferesViewSet, PasajerosViewSet, BusesViewSet, TrayectosViewSet, SetTrayectosViewSet, SetBusesViewSet

router = routers.DefaultRouter()

router.register(r'choferes', ChoferesViewSet, base_name=ChoferesViewSet)
router.register(r'pasajeros', PasajerosViewSet, base_name=PasajerosViewSet)
router.register(r'buses', BusesViewSet, base_name=BusesViewSet)
router.register(r'trayectos', TrayectosViewSet, base_name=TrayectosViewSet)
router.register(r'trayectoSet', SetTrayectosViewSet, base_name=SetTrayectosViewSet)
router.register(r'BusSet', SetBusesViewSet, base_name=SetBusesViewSet)