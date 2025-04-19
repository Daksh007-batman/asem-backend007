from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('profiles', ProfileViewSet)

urlpatterns =[
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls