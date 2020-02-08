from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)

    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    slug = models.SlugField(unique=True, allow_unicode=True)

    description = models.TextField(editable=True)

    date = models.DateTimeField(default=now, editable=False)

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    objects = models.Manager()

    def pubdate(self):
        return self.date.strftime('%b, %d, %Y')

    def __str__(self):
        return self.name
