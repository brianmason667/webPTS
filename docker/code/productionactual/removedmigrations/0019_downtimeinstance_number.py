# Generated by Django 3.1.6 on 2021-03-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0018_auto_20210322_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='downtimeinstance',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
