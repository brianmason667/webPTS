# Generated by Django 3.1.6 on 2021-02-15 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssemblyLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionActual',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular ProductionActual', primary_key=True, serialize=False)),
                ('pa_date', models.DateTimeField(verbose_name='production actual date')),
                ('shift', models.IntegerField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Flex')], default=0)),
                ('assembly_line_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.assemblyline')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PartNumber', models.CharField(max_length=15)),
                ('TeamMember', models.CharField(max_length=2)),
                ('CycleTime', models.CharField(max_length=4)),
                ('AssemblyLine_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.assemblyline')),
            ],
            options={
                'ordering': ['AssemblyLine_ID', 'PartNumber', 'TeamMember', 'CycleTime'],
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=40)),
                ('machine_name_short', models.CharField(max_length=5)),
                ('machine_name_actual', models.CharField(max_length=7)),
                ('AssemblyLine_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.assemblyline')),
            ],
        ),
        migrations.CreateModel(
            name='Hourly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour1', models.IntegerField(default=0)),
                ('hour2', models.IntegerField(default=0)),
                ('hour3', models.IntegerField(default=0)),
                ('hour4', models.IntegerField(default=0)),
                ('hour5', models.IntegerField(default=0)),
                ('hour6', models.IntegerField(default=0)),
                ('hour7', models.IntegerField(default=0)),
                ('hour8', models.IntegerField(default=0)),
                ('hour9', models.IntegerField(default=0)),
                ('hour10', models.IntegerField(default=0)),
                ('hour11', models.IntegerField(default=0)),
                ('hour12', models.IntegerField(default=0)),
                ('ProductionActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.productionactual')),
            ],
        ),
        migrations.CreateModel(
            name='Downtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FourM', models.CharField(max_length=7)),
                ('downtime_code', models.CharField(max_length=5)),
                ('planned', models.BooleanField(default=False)),
                ('downtime_description', models.CharField(max_length=50)),
                ('AssemblyLine_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.assemblyline')),
                ('Machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FourM', models.CharField(max_length=7)),
                ('defect_code', models.CharField(max_length=10)),
                ('defect_description', models.CharField(max_length=50)),
                ('AssemblyLine_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.assemblyline')),
                ('Machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.machine')),
            ],
        ),
        migrations.AddField(
            model_name='assemblyline',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productionactual.department'),
        ),
    ]