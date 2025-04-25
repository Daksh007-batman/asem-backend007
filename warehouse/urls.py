from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('site', SiteViewSet)
router.register('area', AreaViewSet)
router.register('manager', SiteManagerViewSet)
router.register('homegatewayid', HomeIdGatewayViewSet)
router.register('service', ServiceViewSet)

urlpatterns = [] + router.urls   