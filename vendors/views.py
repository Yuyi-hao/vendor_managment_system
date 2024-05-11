from django.shortcuts import render
from .models import Vendor, PurchaseOrder, VendorPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
from rest_framework import viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import * 
from rest_framework import status
import datetime
# Create your views here.

class vendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk):
        performance_metrics = VendorPerformance.objects.all().filter(Vendor_id = pk)
        performance_metrics_serializer = VendorPerformanceSerializer(performance_metrics, many=True)
        return Response(performance_metrics_serializer.data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk):
        # get purchase order 
        try:
            purchase_order = PurchaseOrder.objects.get(id=pk)
        except PurchaseOrder.DoesNotExist:
            return Response(data={'error': 'Item not found'}, status=status.HTTP_400_NOT_FOUND)
        
        # acknowledge purchase order 
        acknowledgment_data = {'acknowledgment_date': datetime.now()}
        purchase_order_updated = PurchaseOrderSerializer(purchase_order, data=acknowledgment_data, partial=True)
        purchase_order_updated.is_valid(raise_exception=True)
        purchase_order_updated.save()

        # return 201 code if updated successfully 
        return Response(data={'message': 'updated purchase order and vendor performance matrices'}, status=status.HTTP_201_CREATED)

    
    