from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(
        verbose_name='category name', max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    cat_image = models.ImageField(
        upload_to='photos/categories', verbose_name='Category Image', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat_name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField(null=True)
    images = models.ImageField(upload_to='photos/products', null=True)
    stock = models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    def get_url(self):
        return reverse("product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
