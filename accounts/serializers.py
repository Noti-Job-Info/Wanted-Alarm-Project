from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email', 
            'phone_number', 
            'device_uuid', 
            'is_admin', 
            'is_active'
            )
