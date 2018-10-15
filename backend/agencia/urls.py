from django.conf.urls import include, url
from . import views
from .routers import router

urlpatterns = [
    url(r'^api/', include(router.urls)),
]