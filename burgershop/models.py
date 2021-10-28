from django.db import models
from django.urls import reverse


class Panel(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('panel', kwargs={'slug': self.name})


class Menu(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('menu', kwargs={'slug': self.title})


class About(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)


