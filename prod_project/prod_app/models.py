from django.contrib.auth.models import User
from django.db import models


class Chemical(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Chemical Name')

    def __str__(self):
        return self.name


class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    date_produced = models.DateField(verbose_name='Production Date')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Update Date')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='batch_creators')
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='batch_updaters')

    def __str__(self):
        return f"Batch from {self.date_produced}"


class ReagentContainer(models.Model):
    id = models.AutoField(primary_key=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, verbose_name='Related Batch')
    container_number = models.IntegerField(null=True, blank=True, default=0, verbose_name='Container number')
    volume = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name='Volume (liters)')
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE, verbose_name='Chemical')
    production = models.BooleanField(verbose_name='Production')
    approved = models.BooleanField(null=True, blank=True, verbose_name='Approved')

    def __str__(self):
        return f"Container {self.container_number} for {self.chemical}"
