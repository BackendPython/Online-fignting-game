# Generated by Django 4.1.2 on 2022-10-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0003_rename_userprofile_profile_rename_img_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='customeuser',
            name='image',
            field=models.ImageField(default='static/images/user.png', upload_to=''),
        ),
    ]
