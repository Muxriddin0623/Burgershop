# Generated by Django 3.2.8 on 2021-10-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burgershop', '0002_menu_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='About')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
