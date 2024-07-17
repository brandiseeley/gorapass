# Generated by Django 5.0.7 on 2024-07-17 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorapass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stamps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_number', models.IntegerField(unique=True)),
                ('spp_number', models.TextField()),
                ('stamp_name', models.TextField(unique=True)),
                ('elevation', models.IntegerField()),
                ('elevation_unit', models.TextField()),
                ('alpine_club', models.TextField()),
                ('region', models.TextField()),
                ('route_type', models.TextField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('completed_at_date', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Hikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hike_name', models.TextField()),
                ('hike_link', models.URLField()),
                ('starting_point', models.TextField()),
                ('starting_point_elevation', models.IntegerField()),
                ('starting_point_elevation_units', models.TextField()),
                ('lat_start', models.FloatField()),
                ('lon_start', models.FloatField()),
                ('ending_point', models.TextField()),
                ('ending_point_elevation', models.IntegerField()),
                ('ending_point_elevation_units', models.TextField()),
                ('lat_end', models.FloatField()),
                ('lon_end', models.FloatField()),
                ('total_elevation_gain', models.IntegerField()),
                ('total_elevation_gain_units', models.TextField()),
                ('difficulty_level', models.TextField()),
                ('recommended_equipment_summer', models.TextField()),
                ('recommended_equipment_winter', models.TextField()),
                ('page_views', models.IntegerField()),
                ('directions_to_start', models.TextField()),
                ('hike_description', models.TextField()),
                ('completed_at_date', models.TimeField()),
                ('stamp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gorapass.stamps', to_field='stamp_name')),
            ],
        ),
    ]
