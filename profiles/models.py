from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class Profile(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('orgadmin', 'Org Admin'),
        ('viewer', 'Viewer')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    ...