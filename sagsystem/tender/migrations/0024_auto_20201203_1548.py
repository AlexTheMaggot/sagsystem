# Generated by Django 3.1.1 on 2020-12-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0023_auto_20201130_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='cpo_confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tender',
            name='cpo_confirm_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
