# Generated by Django 4.1.5 on 2023-01-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksinventory', '0002_book_delete_bookinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
