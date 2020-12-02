from django.urls import path
from .views import DecodeVIN, HistoryOfAccessedVIN

urlpatterns = [
    path('details/<vin>', DecodeVIN.as_view()),
    path('history', HistoryOfAccessedVIN.as_view()),
]
