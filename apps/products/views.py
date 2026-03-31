from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductColourViewSet(ModelViewSet):
    queryset = ProductColour.objects.all()
    serializer_class = ProductColourSerializer


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductSizeViewSet(ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductReviewViewSet(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer