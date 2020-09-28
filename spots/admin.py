from django.contrib import admin
from .models import Category, Spot, SpotImage, Bookmark


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'enabled')


class SpotImageInline(admin.TabularInline):
    model = SpotImage
    extra = 2


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    inlines = [SpotImageInline, ]
    list_display = ('id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at', 'enabled')


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_id')
