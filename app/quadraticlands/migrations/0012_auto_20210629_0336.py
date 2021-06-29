# Generated by Django 2.2.21 on 2021-06-29 03:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadraticlands', '0011_remove_gameplayer_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamefeed',
            name='action',
            field=models.CharField(blank=True, db_index=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='cached_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
