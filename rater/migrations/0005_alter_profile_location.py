# Generated by Django 4.0.5 on 2022-06-12 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0004_remove_rating_average_rating_remove_rating_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Nairobi', max_length=100),
        ),
    ]