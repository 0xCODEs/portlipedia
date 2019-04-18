# Generated by Django 2.1.1 on 2019-04-16 02:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('port', models.IntegerField(validators=[django.core.validators.MaxValueValidator(65536), django.core.validators.MinValueValidator(1)])),
                ('protocol', models.CharField(max_length=3)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]