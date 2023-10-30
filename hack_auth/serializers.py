from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=28, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def validate(self, attrs):
        username = attrs.get('username', '')
        email =    attrs.get('email', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                "The username should only contain alphanumeric characters")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

#class EmailVerifySerializer(serializers.ModelSerializer):
    #pass
