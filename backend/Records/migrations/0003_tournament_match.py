# Generated by Django 5.1.4 on 2024-12-10 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Records", "0002_player_totalmatch_player_totalwins"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("t_name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("cardgame", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("player1", models.CharField(max_length=100)),
                ("player2", models.CharField(max_length=100)),
                ("winner", models.CharField(blank=True, max_length=100, null=True)),
                ("match_date", models.DateTimeField(auto_now_add=True)),
                ("round", models.IntegerField()),
                (
                    "player1id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches1_id",
                        to="Records.player",
                    ),
                ),
                (
                    "player2id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches2_id",
                        to="Records.player",
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches",
                        to="Records.tournament",
                    ),
                ),
            ],
        ),
    ]
