from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperAdmin
from .serializer import ProfileSerializer

class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    queryset = Profile.objects.exclude(role = 'superadmin')
    serializer_class = ProfileSerializer