# Generated by Django 3.2.8 on 2021-10-24 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burgershop', '0010_auto_20211024_2053'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
