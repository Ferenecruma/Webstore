from django.db import models
from django.utils.timezone import now
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, to_lower=True)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, editable=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, to_lower=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)

    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, editable=False)

    image = models.ImageField(upload_to='images/', default="default.jpg")

    description = models.TextField(editable=True)

    date = models.DateTimeField(default=now, editable=False)

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    objects = models.Manager()

    def pubdate(self):
        return self.date.strftime('%b, %d, %Y')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
