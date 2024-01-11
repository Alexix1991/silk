# Generated by Django 4.2.9 on 2024-01-11 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duties',
            name='crop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='duties.crops', unique=True),
        ),
    ]
