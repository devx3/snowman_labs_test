from rest_framework.routers import SimpleRouter
from .views import SpotsViewSet, CategoriesViewSet, BookmarksViewSet, SearchViewSet

router = SimpleRouter()
router.register('spots', SpotsViewSet, basename='spots')
router.register('search', SearchViewSet, basename='search')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('bookmarks', BookmarksViewSet, basename='bookmarks')
