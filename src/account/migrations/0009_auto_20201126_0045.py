# Generated by Django 2.2.15 on 2020-11-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20201126_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='lcno',
            field=models.CharField(max_length=30, null=True, verbose_name='lcno'),
        ),
    ]
