# Generated by Django 3.2.3 on 2021-06-08 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ota_app2', '0003_auto_20210608_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='rateplan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='ota_app2.rateplan'),
        ),
    ]
