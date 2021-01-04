# Generated by Django 3.1.4 on 2021-01-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0022_auto_20201210_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='selectedprice',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
