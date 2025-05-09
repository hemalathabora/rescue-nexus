# Generated by Django 5.0.7 on 2025-03-16 15:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_app', '0004_alter_foodrequest_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=255)),
                ('food_type', models.CharField(choices=[('cooked', 'Cooked Food'), ('dry', 'Dry Rations'), ('baby', 'Baby Food')], max_length=50)),
                ('quantity', models.IntegerField()),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='food_images/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
