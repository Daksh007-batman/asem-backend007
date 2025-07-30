from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path

router = DefaultRouter()
router.register('site', SiteViewSet)
router.register('area', AreaViewSet)
router.register('manager', SiteManagerViewSet)
router.register('homegatewayid', HomeIdGatewayViewSet)
router.register('service', ServiceViewSet)

urlpatterns = [
    path('customerlist/', ListAllcustomer.as_view())
] + router.urls   