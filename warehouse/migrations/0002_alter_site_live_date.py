# Generated by Django 5.2 on 2025-04-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='live_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
