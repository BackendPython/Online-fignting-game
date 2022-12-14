# Generated by Django 4.1.2 on 2022-10-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0008_customeuser_defeats_customeuser_victory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_players', models.IntegerField(default=0)),
                ('first_player', models.CharField(max_length=50)),
                ('second_player', models.CharField(max_length=50)),
                ('player_heal', models.IntegerField(default=100)),
                ('player_attack', models.IntegerField(default=10)),
                ('player_jump', models.BooleanField(default=False)),
                ('player_winner', models.BooleanField(default=False)),
                ('player_blow_turn', models.BooleanField(default=False)),
                ('rival_heal', models.IntegerField(default=100)),
                ('rival_attack', models.IntegerField(default=10)),
                ('rival_jump', models.BooleanField(default=False)),
                ('rival_winner', models.BooleanField(default=False)),
                ('rival_blow_turn', models.BooleanField(default=False)),
            ],
        ),
    ]
