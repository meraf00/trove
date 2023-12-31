# Generated by Django 4.2.5 on 2023-09-13 08:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image_url', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('products', models.ManyToManyField(to='product_api.product')),
            ],
        ),
    ]
