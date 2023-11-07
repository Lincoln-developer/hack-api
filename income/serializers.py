from rest_framework import serializers
from hack_auth.models import User

class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','date','source', 'amount', 'description']