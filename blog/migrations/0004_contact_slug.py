# Generated by Django 3.2.8 on 2021-10-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(default=0, unique=True, verbose_name='Url'),
            preserve_default=False,
        ),
    ]