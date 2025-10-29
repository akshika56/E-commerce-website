# backend/govindtoys/shop/views.py

from rest_framework import viewsets
from .models import Product, Order, Review
from .serializers import ProductSerializer, OrderSerializer, ReviewSerializer


# ✅ Product API (CRUD)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')  # Show latest first
    serializer_class = ProductSerializer


# ✅ Order API
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer


# ✅ Review API
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
