from django.urls import path, include
from rest_framework import routers 
from .views import vendorViewSet, PurchaseOrderViewSet

router = routers.DefaultRouter()
router.register(r'vendors', vendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]