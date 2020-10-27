# Generated by Django 3.1.1 on 2020-10-12 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0009_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.product'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tender.provider'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='tender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tender.tender'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='tender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tender.tender'),
        ),
    ]