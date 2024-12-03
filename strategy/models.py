from django.db import models

# models.py
from django.db import models

class Strategy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class KPI(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_value = models.FloatField()
    current_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)