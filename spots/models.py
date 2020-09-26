from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.name


class Spot(Base):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='spots', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class SpotImage(Base):
    spot = models.ForeignKey(Spot, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        blank=True, upload_to='photos/%Y/%m/')

    def __str__(self):
        return self.image.name


class FavoriteSpot(Base):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return self.spot.name
