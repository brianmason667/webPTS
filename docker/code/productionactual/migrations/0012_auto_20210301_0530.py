# Generated by Django 3.1.6 on 2021-03-01 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0011_auto_20210301_0529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='RunNumber',
            new_name='number',
        ),
    ]
