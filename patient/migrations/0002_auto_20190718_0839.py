# Generated by Django 2.2.3 on 2019-07-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Pt_name',
            field=models.CharField(max_length=50),
        ),
    ]
