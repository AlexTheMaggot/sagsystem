# Generated by Django 3.1.1 on 2020-10-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0003_product_measure'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
