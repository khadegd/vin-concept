from django.db import models

class Vehical(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    data = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
