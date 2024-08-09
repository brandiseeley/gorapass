# Generated by Django 5.0.6 on 2024-08-02 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorapass', '0015_remove_hikes_stamp_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CompletedStamps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gorapass.stamps')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gorapass.users')),
            ],
        ),
        migrations.AddConstraint(
            model_name='completedstamps',
            constraint=models.UniqueConstraint(fields=('stamp_id', 'user_id'), name='unique_stamp_to_user'),
        ),
    ]