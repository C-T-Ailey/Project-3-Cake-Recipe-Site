# Generated by Django 4.0.5 on 2022-06-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_date',
            field=models.DateTimeField(verbose_name='time and date created'),
        ),
    ]
