import requests
import json
from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from vin.models import Vehical
from .serializers import VehicalSerializer

class DecodeVIN(APIView):
    """
    Check if VIN is valid.
    Shows latest accessed vin in last 6 hours.
    If not present get, freshly decoded.
    """

    def get(self, request, vin, format=None):
        is_valid_vin = ValidateVIN(vin).is_valid_vin()

        if not is_valid_vin:
            return Response('Not a valid vin')

        time_threshold = datetime.now() - timedelta(hours=6)
        latest_accessed_vin = Vehical.objects.filter(updated_at__lt=time_threshold,vin=vin)

        if not latest_accessed_vin:
            decoded_vins = self.fetch_from_nhtsa(vin)
            for vehical in decoded_vins:
                latest_accessed_vin = vehical
                obj, created = Vehical.objects.update_or_create(
                    vin=vehical['VIN'], data=vehical
                )
        return Response(latest_accessed_vin)

    def fetch_from_nhtsa(self, vin):
        nhtsa_url = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/"
        payload = {
            'data': vin,
            'format': 'json'
        }
        _response = requests.post(nhtsa_url, payload)
        _results = json.loads(_response.content)
        results = _results['Results']
        return results


class HistoryOfAccessedVIN(generics.ListAPIView):
    queryset = Vehical.objects.all().order_by('-updated_at')[:255]
    serializer_class = VehicalSerializer

class ValidateVIN():
    def __init__(self, vin):
        self.vin = vin

    def is_valid_vin(self):
        if not self.is_length_valid:
            return False

        calculated_check_digit = self.calculate_check_digit(self.vin);

        if self.vin[8] == 'X':
            return True if calculated_check_digit == self.vin[8] else False
        else:
            return True if calculated_check_digit == int(self.vin[8]) else False


    def is_length_valid(self):
        return True if len(self.vin) else False

    def calculate_check_digit(self, vin):
        total = 0;
        for i in range(len(vin)):
            total += self.decode_value_of(vin[i]) * self.get_weight_of(i)
        result = total % 11
        return X if result == 10 else result

    def decode_value_of(self, char):
        return '0123456789.ABCDEFGH..JKLMN.P.R..STUVWXYZ'.index(char) % 10

    def get_weight_of(self, index):
        # weights assigned for each 17 digits
        weights = '8765432X098765432'
        # every weight stands for it's own value
        # except x represents 10
        values = '0123456789X'
        return values.index(weights[index])

