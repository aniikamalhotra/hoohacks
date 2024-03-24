# Generated by Django 5.0.3 on 2024-03-23 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='volume_at_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(default=0, max_length=10)),
                ('volume', models.CharField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='volume_dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vDataset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='DataEntry', to='airsafeapp.volume_at_time')),
            ],
        ),
    ]