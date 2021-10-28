from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=300, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='blog/photos/%Y/%m/%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

