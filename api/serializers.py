from rest_framework import serializers
from rest_framework.response import Response

from vin.models import Vehical

class VehicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehical
        fields = ['vin', 'data', 'created_at', 'updated_at']
