from rest_framework import serializers
from .models import Category, Spot, SpotImage, Bookmark


class SpotImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotImage
        fields = ('id', 'image', 'spot', 'created_at', 'updated_at', 'enabled')


class SpotSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Spot
        fields = (
            'id',
            'name',
            'category',
            'latitude',
            'longitude',
            'images',
            'created_at',
            'updated_at',
            'enabled',
        )


class CategorySerializer(serializers.ModelSerializer):
    spots = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'spots',
            'created_at',
            'updated_at',
            'enabled',
        )


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = (
            'id',
            'user',
            'spot',
        )
