import requests
from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from vin.models import Vehical

class DecodeVIN(APIView):
    """
    Check if VIN is valid.
    Shows latest accessed vin in last 6 hours.
    If not present get, freshly decoded.
    """

    def get(self, request, vin, format=None):
        time_threshold = datetime.now() - timedelta(hours=6)
        latest_accessed_vin = Vehical.objects.filter(updated_at__lt=time_threshold,vin=vin)

        if latest_accessed_vin is None:
            fetch_from_nhtsa = None
        return Response(latest_accessed_vin)

class HistoryOfAccessedVIN(APIView):
    def get(self, request, format=None):
        history = Vehical.objects.all().order_by('-updated_at')[:255]
        return Response(history)
