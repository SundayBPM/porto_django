# Generated by Django 5.1.3 on 2024-11-28 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tittle',
            new_name='title',
        ),
    ]
