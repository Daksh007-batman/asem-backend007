from django.shortcuts import render
from rest_framework.viewsets  import ModelViewSet
from profiles.permissions import IsSuperAdmin
from .models import *
from .serializers import *
# Create your views here.

class SiteViewSet(ModelViewSet):
    permission_classes = [IsSuperAdmin]
    queryset = Site.objects.all()
    serializer_class = SiteSerializer