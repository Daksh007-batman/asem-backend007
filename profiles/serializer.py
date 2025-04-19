from rest_framework.serializers import ModelSerializer, CharField
from .models import Profile

class ProfileSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'role', 'is_active', 'password']
    
    def create(self, validated_data:dict):
        user = Profile(
            email=validated_data['email'],
            username=validated_data['username'],
            role = validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user