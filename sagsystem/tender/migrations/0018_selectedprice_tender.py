# Generated by Django 3.1.1 on 2020-10-24 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0017_selectedprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedprice',
            name='tender',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='tender.tender'),
            preserve_default=False,
        ),
    ]