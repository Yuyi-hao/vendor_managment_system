from rest_framework import serializers
from .models import Vendor, PurchaseOrder, VendorPerformance
from django.utils import timezone
from rest_framework.response import Response
from django.db import models


class VendorSerializer(serializers.ModelSerializer):
    vendor_id = serializers.ReadOnlyField()
    class Meta:
        model = Vendor
        fields = "__all__"

    def create(self, validated_data):
        vendor = Vendor.objects.create(
            name = validated_data['name'],
            contact_details = validated_data['contact_details'],
            address = validated_data['address'],
            vendor_code = validated_data['vendor_code'],
            on_time_delivery_rate = validated_data['on_time_delivery_rate'],
            quality_rating_avg = validated_data['quality_rating_avg'],
            average_response_time = validated_data['average_response_time'],
            fulfillment_rate = validated_data['fulfillment_rate']
        )
        vendor.save()

        vendor_performance  = VendorPerformance.objects.create(
            Vendor = vendor,
            date = timezone.now(),
            on_time_delivery_rate = validated_data['on_time_delivery_rate'],
            quality_rating_avg = validated_data['quality_rating_avg'],
            average_response_time = validated_data['average_response_time'],
            fulfillment_rate = validated_data['fulfillment_rate']
        )
        vendor_performance.save()
        return vendor
    

class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchaseOrder_id = serializers.ReadOnlyField()
    class Meta:
        model = PurchaseOrder
        fields = "__all__"

class VendorPerformanceSerializer(serializers.ModelSerializer):
    # vendorPerformance_id = serializers.ReadOnlyField()
    class Meta:
        model = VendorPerformance
        fields = "__all__"