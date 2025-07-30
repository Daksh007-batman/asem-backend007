from platform import node
from django.shortcuts import render
from rest_framework.viewsets  import ModelViewSet
from rest_framework.decorators import APIView
from profiles.permissions import IsSuperAdmin
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.status import *
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

class ListAllcustomer(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
            customer_id = request.query_params.get('customer')
            if customer_id is None:
                raise ValidationError("This query parameter is required.")

            if not Profile.objects.filter(pk=customer_id).exists():
                raise ValidationError("Customer not found")

            sites = (
                Site.objects
                    .filter(customer_id=customer_id)
                    # .values_list('id', flat=True)
            )
            serialized = SiteSerializer(sites, many=True)
            print(serialized)
            resp = [
                {
                     "site_name": i["name"],
                    "site_type": i["site_type"],
                    "site_location": i["location"],
                    "site_manager": i["site_manager"],
                } 
                for i in serialized.data
            ]

            return Response({"data": resp}, status=HTTP_200_OK)
    