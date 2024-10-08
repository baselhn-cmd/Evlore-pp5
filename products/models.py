from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
            max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            # Convert the ratings to float for proper summing
            total_ratings = sum(float(review.rating) for review in reviews)
            return total_ratings / len(reviews)
            return 0

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(
            Product, on_delete=models.CASCADE, related_name='wishlists')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Review(models.Model):
    Product = models.ForeignKey(
            Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=3)
    content = models.TextField()
    created_by = models.ForeignKey(
            User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content} - {self.created_by.username}'
