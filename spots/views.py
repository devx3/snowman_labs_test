from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404


from .models import Spot, Category, SpotImage, Bookmark
from .serializers import (
    SpotSerializer,
    CategorySerializer,
    SpotImageSerializer,
    BookmarkSerializer,
)


class SpotsViewSet(viewsets.ModelViewSet):
    """
    The SpotsViewSet
    """
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

    @action(detail=True, methods=['get', 'delete'])
    def images(self, request, pk=None):
        if request.method == 'GET':
            images = SpotImage.objects.filter(spot_id=pk)
            serializer = SpotImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'DELETE':
            image_id = request.GET.get('image_id')
            result, image = SpotImage.objects.filter(id=image_id).delete()
            if result > 0:
                return Response({'Image was deleted'}, status=status.HTTP_200_OK)
            return Response({'Image not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        data = request.data
        data['spot'] = pk
        file_serializer = SpotImageSerializer(data=data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchViewSet(mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    This viewset provides the search spot functionality
    """

    def list(self, request):
        return Response(data={'msg': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk):
        queryset = Spot.objects.filter(Q(name__icontains=pk))
        serializer = SpotSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    Create, Update, List and Remove Categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookmarksViewSet(viewsets.ModelViewSet):
    """
    BookmarksViewSet
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Bookmark.objects.filter(user_id=self.request.user)
        return Bookmark.objects.none()

    def create(self, request):
        if self.request.user.is_authenticated:
            try:
                spot = request.data['spot']
            except KeyError:
                spot = None

            data = {
                'user': request.user.id,
                'spot': spot
            }
            serializer = BookmarkSerializer(data=data)
            if serializer.is_valid():

                # First we need to verify if spot is already marked as bookmark for this user
                obj = Bookmark.objects.filter(
                    spot_id=data['spot'],
                    user_id=data['user']
                )
                if not len(obj) > 0:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        'msg': 'This spot is already in your bookmark'
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if request.user.is_authenticated:
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                return Response({'msg': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({
                'msg': f'{instance} deleted from bookmarks.'
            }, status=status.HTTP_204_NO_CONTENT)
