# Generated by Django 3.1.6 on 2021-03-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0013_auto_20210301_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ToteQuantity',
            field=models.IntegerField(default=0),
        ),
    ]
