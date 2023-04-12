# Generated by Django 2.2.15 on 2020-12-16 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialist', models.TextField(max_length=500)),
                ('lcno', models.TextField(max_length=50)),
                ('address', models.TextField(max_length=500)),
                ('phone', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=doctor.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
