# Generated by Django 4.1.5 on 2023-01-25 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksinventory', '0003_animal'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Animal',
        ),
    ]