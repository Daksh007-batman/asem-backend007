from django.shortcuts import render
from rest_framework.viewsets  import ModelViewSet
from rest_framework.decorators import api_view
from profiles.permissions import IsSuperAdmin
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.

class SiteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        customer_id = self.request.query_params.get('customer')
        if customer_id:
            queryset = queryset.filter(customer_id=customer_id)
        return queryset


class AreaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        site_id = self.request.query_params.get('site')
        if site_id:
            queryset = queryset.filter(site_id=site_id)
        return queryset

class SiteManagerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = SiteManager.objects.all()
    serializer_class = SiteManagerSerializer


class ServiceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        site_id = self.request.query_params.get('site')
        if site_id:
            queryset = queryset.filter(site_id=site_id)
        return queryset


class HomeIdGatewayViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = HomeGatewayId.objects.all()
    serializer_class = HomeGatewayIdSerializer

