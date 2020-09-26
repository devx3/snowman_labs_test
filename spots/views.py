from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Spot, Category, SpotImage, FavoriteSpot
from .serializers import (
    SpotSerializer,
    CategorySerializer,
    SpotImageSerializer,
    FavoriteSpotsSerializer,
)


class SpotsViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        images = SpotImage.objects.filter(spot_id=pk)
        serializer = SpotImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        file_serializer = SpotImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    Create, Update, List and Remove Categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FavoriteSpotsViewSet(viewsets.ModelViewSet):
    """
    List all favorite spots
    """
    queryset = FavoriteSpot.objects.all()
    serializer_class = FavoriteSpotsSerializer
