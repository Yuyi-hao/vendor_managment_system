from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    quality_rating_avg = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=(('pending', 'Pending'),( 'completed', 'Completed'), ('canceled','Canceled')))
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.po_number

class VendorPerformance(models.Model):
    Vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    date = models.DateField()
    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    quality_rating_avg = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])