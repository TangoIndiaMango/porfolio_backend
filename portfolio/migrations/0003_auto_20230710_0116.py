# Generated by Django 3.1.4 on 2023-07-10 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20230709_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmodel',
            old_name='tools',
            new_name='tool',
        ),
    ]