from django.db import models


class CurrencyData(models.Model):
    currency = models.CharField(max_length=100)
    value = models.FloatField()
    rate = models.FloatField()

    def __str__(self):
        return self.currency
