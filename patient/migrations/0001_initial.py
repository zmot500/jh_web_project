# Generated by Django 2.2.3 on 2019-07-17 23:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('Pt_name', models.TextField()),
                ('Pt_bdate', models.DateField()),
                ('Pt_man', models.BooleanField(default=True)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('in_date', models.DateField()),
                ('in_db', models.IntegerField()),
                ('in_wt', models.DecimalField(decimal_places=2, max_digits=5)),
                ('in_bp_l', models.IntegerField()),
                ('in_bp_h', models.IntegerField()),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
    ]