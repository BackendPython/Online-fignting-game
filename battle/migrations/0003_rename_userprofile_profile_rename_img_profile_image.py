# Generated by Django 4.1.2 on 2022-10-18 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='img',
            new_name='image',
        ),
    ]
