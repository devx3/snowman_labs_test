from rest_framework.routers import SimpleRouter
from .views import SpotsViewSet, CategoriesViewSet

router = SimpleRouter()
router.register('spots', SpotsViewSet, basename='spots')
router.register('categories', CategoriesViewSet, basename='categories')
