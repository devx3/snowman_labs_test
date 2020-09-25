from django.db import models


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
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    category = models.ForeignKey(Category, related_name='spot', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class SpotImage(Base):
    spot = models.ForeignKey(Spot, related_name='images', on_delete=models.DO_NOTHING)
    image = models.ImageField(
        blank=True, upload_to='photos/%Y/%m/')

    def __str__(self):
        return self.image.name
