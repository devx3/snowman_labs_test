from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Spot, Category, SpotImage
from .serializers import (
    SpotSerializer,
    CategorySerializer,
    SpotImageSerializer,
)


class SpotsViewSet(viewsets.ModelViewSet):
    """
    The SpotsViewSet
    """
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        images = SpotImage.objects.filter(spot_id=pk)
        serializer = SpotImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        data = request.data
        data['spot'] = pk
        file_serializer = SpotImageSerializer(data=data)

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
