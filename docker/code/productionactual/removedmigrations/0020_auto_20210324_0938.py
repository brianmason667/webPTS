# Generated by Django 3.1.6 on 2021-03-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0019_downtimeinstance_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='downtimeinstance',
            name='finish_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='downtimeinstance',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]