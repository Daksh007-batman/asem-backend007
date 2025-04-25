from rest_framework.serializers import ModelSerializer
from .models import Site, Service, SiteManager, Area, HomeGatewayId

class SiteSerializer(ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
    

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class SiteManagerSerializer(ModelSerializer):
    class Meta:
        model = SiteManager
        fields = '__all__'


class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

    def create(self, validated_data:dict):
        if 'shows_on' not in validated_data:
            validated_data['shows_on'] =  validated_data['site']
        return super().create(validated_data)
    
    def update(self, instance, validated_data:dict):
        if 'shows_on' not in validated_data:
            validated_data['shows_on'] = validated_data.get('site', instance.site)
        return super().update(instance, validated_data)


class HomeGatewayIdSerializer(ModelSerializer):
    class Meta:
        model = HomeGatewayId
        fields = '__all__'

