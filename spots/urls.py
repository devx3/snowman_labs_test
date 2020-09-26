from rest_framework.routers import SimpleRouter
from .views import SpotsViewSet, CategoriesViewSet, FavoriteSpotsViewSet

router = SimpleRouter()
router.register('spots', SpotsViewSet, basename='spots')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('favorites', FavoriteSpotsViewSet, basename='favorites') 
# router.register('images', SpotImagesViewSet, basename='images')
