from rest_framework import routers
from agencia.viewsets import ChoferesViewSet, PasajerosViewSet, BusesViewSet, TrayectosViewSet

router = routers.DefaultRouter()

router.register(r'choferes', ChoferesViewSet, base_name=ChoferesViewSet)
router.register(r'pasajeros', PasajerosViewSet, base_name=PasajerosViewSet)
router.register(r'buses', BusesViewSet, base_name=BusesViewSet)
router.register(r'trayectos', TrayectosViewSet, base_name=TrayectosViewSet)