# Generated by Django 3.1.1 on 2020-10-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0006_auto_20201007_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
