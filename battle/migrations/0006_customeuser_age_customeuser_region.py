# Generated by Django 4.1.2 on 2022-10-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0005_customeuser_bio_alter_customeuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='age',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='customeuser',
            name='region',
            field=models.CharField(default='Uzbekistan', max_length=50),
        ),
    ]