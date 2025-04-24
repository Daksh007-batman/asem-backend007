from rest_framework.routers import DefaultRouter
from .views import SiteViewSet

router = DefaultRouter()
router.register('site', SiteViewSet)

urlpatterns = [] + router.urls