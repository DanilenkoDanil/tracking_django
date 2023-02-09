from django.db import models


class Signal(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    price = models.FloatField(default=0)
    source = models.CharField(default=' ', max_length=100)
    date = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class SignalResult(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    price = models.FloatField(default=0)
    price_change = models.FloatField(default=0)
    source = models.CharField(default=' ', max_length=100)
    date = models.DateTimeField(auto_created=True, auto_now=True)


class Marathon(models.Model):
    channel = models.CharField(max_length=200)
    current_balance = models.FloatField()
    start_balance = models.FloatField()
    leverage = models.FloatField(default=1)


class Setting(models.Model):
    channel_for_bot = models.CharField(max_length=200)
