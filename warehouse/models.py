from django.db import models
from profiles.models import Profile

# Create your models here.

class SiteManager(models.Model):
    name = models.CharField(max_length = 100, blank = False, null= False)
    email = models.EmailField(max_length = 50, blank = True, null = False)
    phone_number = models.CharField(max_length=15, blank = True, null = False)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length = 100, null = False, blank = False)
    customer = models.ForeignKey(to = Profile, on_delete=models.CASCADE, null = False, blank = False, default = 1)
    SITE_TYPE_CHOICES  = [
        ("whtm", "Warehouse Total Metering"),
        ("savings", "Warehouse Savings"),
        ("submetering", "Warehouse Submetering"),
        ("fems", "Equipment Management"),
        ("firemonitor", "Fire Monitoring System")
    ]
    site_type = models.CharField(max_length=100, choices = SITE_TYPE_CHOICES, default = "savings")
    location = models.CharField(max_length=100, blank = False, null = True)
    is_active = models.BooleanField(default = False)
    is_live = models.BooleanField(default=False)
    live_date = models.DateTimeField(blank = True, null = True)
    site_manager = models.ForeignKey(to = SiteManager, on_delete=models.CASCADE, blank = True,  default = None, null = True)

    def __str__(self):
        return self.name


class Service(models.Model):
    site = models.ForeignKey(to = Site, null = False, blank = True, on_delete=models.CASCADE)
    power_factor = models.BooleanField(default = False)
    hourly_data = models.BooleanField(default = False)
    load_data_graph = models.BooleanField(default=False)
    alarm_history = models.BooleanField(default = False)
    carbon_emission = models.BooleanField(default = False)
    fuel_data = models.BooleanField(default = False)
    dg_mains_runtime = models.BooleanField(default = False)
    voltage_alarms = models.BooleanField(default = False)

    def __str__(self):
        return self.site.name


class Area(models.Model):
    name = models.CharField(max_length = 100, blank =  False, null = False)
    site = models.ForeignKey(to = Site, on_delete=models.CASCADE)
    shows_on = models.ForeignKey(to = Site, on_delete = models.CASCADE, related_name="shows_on")
    is_active = models.BooleanField(default = False)
    is_live = models.BooleanField(default=False)
    live_date = models.DateTimeField()
    source = models.CharField(max_length = 12, blank = False, null = False, default = "mains")

    def __str__(self):
        return self.name

    
class HomeGatewayId(models.Model):
    home_gatewway_id = models.CharField(max_length=50, blank = False, null= False)
    site = models.ForeignKey(to = Site, on_delete=models.CASCADE)
    rssh_port = models.IntegerField(blank = False, null = False)
    monitoring_port = models.IntegerField(blank = False, null  =  False)
    
    def __str__(self):
        return f'{self.site.name} | {self.home_gateway_id}'