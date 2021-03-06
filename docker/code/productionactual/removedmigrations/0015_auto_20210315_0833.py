# Generated by Django 3.1.6 on 2021-03-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionactual', '0014_product_totequantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['assembly_line', 'PartNumber', 'TeamMember', 'CycleTime']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='AssemblyLine_ID',
            new_name='assembly_line',
        ),
        migrations.AlterField(
            model_name='run',
            name='number',
            field=models.IntegerField(default=1, help_text='Run Number'),
        ),
    ]
