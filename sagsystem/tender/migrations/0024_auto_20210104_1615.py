# Generated by Django 3.1.4 on 2021-01-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0023_auto_20210104_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedprice',
            name='sum',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
