from rest_framework import serializers
from hack_auth.models import User

class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['date', 'id', 'amount', 'description', 'category']