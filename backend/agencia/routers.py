from rest_framework import routers
from agencia.viewsets import choferesCRUDViewSet, pasajerosCRUDViewSet, busesRViewSet, trayectosRViewSet, trayectoCUDViewSet, busCUDViewSet, asientoAsignadoCRUDViewSet # trayectoPasajeroRViewSet

router = routers.DefaultRouter()

router.register(r'choferesCRUD', choferesCRUDViewSet, base_name=choferesCRUDViewSet)
router.register(r'pasajerosCRUD', pasajerosCRUDViewSet, base_name=pasajerosCRUDViewSet)
router.register(r'busesR', busesRViewSet, base_name=busesRViewSet)
router.register(r'trayectosR', trayectosRViewSet, base_name=trayectosRViewSet)

router.register(r'trayectoCUD', trayectoCUDViewSet, base_name=trayectoCUDViewSet)
router.register(r'busCUD', busCUDViewSet, base_name=busCUDViewSet)
router.register(r'asientoAsignadoCRUD', asientoAsignadoCRUDViewSet, base_name=asientoAsignadoCRUDViewSet)
# router.register(r'trayectoPasajeroR', trayectoPasajeroRViewSet, base_name=trayectoPasajeroRViewSet)