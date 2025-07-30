from django.db import models
from warehouse.models import Area

# Create your models here.
class DailyData(models.Model):
    area = models.ForeignKey(to = Area, on_delete=models.CASCADE, blank = False, null = False)
    unit_consumption = models.FloatField()
    date = models.DateField()
    energy_saved = models.FloatField()
    is_visible = models.BooleanField(default = True)


class HourlyData(models.Model):
    area = models.ForeignKey(to = Area, on_delete=models.CASCADE, blank = False, null = False)
    unit_consumption = models.FloatField()
    reading_from = models.DateTimeField()
    reading_to = models.DateTimeField()
    energy_saved = models.FloatField()
    is_visible = models.BooleanField(default = True)