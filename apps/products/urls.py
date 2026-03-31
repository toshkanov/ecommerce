from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet, basename='products')
router.register('product-colours', ProductColourViewSet, basename='product-colours')
router.register('product-images', ProductImageViewSet, basename='product-images')
router.register('product-sizes', ProductSizeViewSet, basename='product-sizes')
router.register('product-reviews', ProductReviewViewSet, basename='product-reviews')
router.register('wishlists', WishlistViewSet, basename='wishlists')

urlpatterns = router.urls