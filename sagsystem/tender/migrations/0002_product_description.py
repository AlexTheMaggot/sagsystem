# Generated by Django 3.1.1 on 2020-10-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
