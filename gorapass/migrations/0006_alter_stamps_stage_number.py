# Generated by Django 5.0.7 on 2024-07-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorapass', '0005_alter_stamps_stage_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stamps',
            name='stage_number',
            field=models.IntegerField(unique=True),
        ),
    ]
