# Generated by Django 5.0.7 on 2024-07-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorapass', '0008_hikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikes',
            name='stamp_name',
            field=models.TextField(),
        ),
    ]
