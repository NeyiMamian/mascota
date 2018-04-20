from django.urls import path, include
from rest_framework import routers
from mascota.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'mascota', mascota_viewset)
router.register(r'cliente', cliente_viewset)
router.register(r'raza', raza_viewset)
router.register(r'servicio',servicio_viewset)

urlpatterns =[
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 