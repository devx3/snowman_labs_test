from django.contrib import admin
from .models import Category, Spot, SpotImage, FavoriteSpot


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'enabled')


class SpotImageInline(admin.TabularInline):
    model = SpotImage
    extra = 2


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    inlines = [SpotImageInline, ]
    list_display = ('name', 'latitude', 'longitude', 'created_at', 'updated_at', 'enabled')


@admin.register(FavoriteSpot)
class FavoriteSpotAdmin(admin.ModelAdmin):
    list_display = ('user', 'spot', 'created_at')
