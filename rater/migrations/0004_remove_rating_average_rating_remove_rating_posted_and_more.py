# Generated by Django 4.0.5 on 2022-06-11 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0003_alter_project_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='posted',
        ),
        migrations.AddField(
            model_name='rating',
            name='creativity_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='content_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
    ]
