# Generated by Django 3.1.6 on 2021-03-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0012_auto_20210301_0530'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='run',
            name='unique run_num',
        ),
        migrations.AddConstraint(
            model_name='run',
            constraint=models.UniqueConstraint(fields=('ProductionActual', 'number'), name='unique number'),
        ),
    ]
