# Generated by Django 3.1.6 on 2021-03-15 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0015_auto_20210315_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defect',
            old_name='AssemblyLine_ID',
            new_name='assembly_line',
        ),
        migrations.RenameField(
            model_name='downtime',
            old_name='AssemblyLine_ID',
            new_name='assembly_line',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='AssemblyLine_ID',
            new_name='assembly_line',
        ),
    ]
