# Generated by Django 3.0 on 2023-03-06 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20230303_0321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('image',)},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={},
        ),
    ]
