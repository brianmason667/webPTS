# Generated by Django 3.1.6 on 2021-03-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0017_auto_20210315_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CycleTime',
            field=models.FloatField(max_length=4),
        ),
    ]
