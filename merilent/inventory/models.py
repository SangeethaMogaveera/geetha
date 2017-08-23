from django.db import models
from django.contrib import admin
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255, blank=True)

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    item_id = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=800)
    vendor_name = models.ForeignKey(Vendor,on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name