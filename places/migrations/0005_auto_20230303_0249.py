# Generated by Django 3.0 on 2023-03-03 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20230303_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place'),
        ),
    ]
