# Generated by Django 3.0 on 2022-08-24 14:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='OldProfile',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
    ]
