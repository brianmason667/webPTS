# Generated by Django 3.1.6 on 2021-02-15 08:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0002_auto_20210215_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionactual',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular ProductionActual', primary_key=True, serialize=False),
        ),
    ]
