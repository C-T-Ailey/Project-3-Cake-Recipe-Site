# Generated by Django 4.0.4 on 2022-06-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_cake_flavours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='flavours',
            field=models.CharField(choices=[('0', 'Plain Sponge'), ('1', 'Caramel'), ('2', 'Chocolate'), ('3', 'Cream Cheese'), ('4', 'Fruit'), ('5', 'Spiced'), ('6', 'Vanilla'), ('7', 'Experimental')], default='0', max_length=20),
        ),
    ]
