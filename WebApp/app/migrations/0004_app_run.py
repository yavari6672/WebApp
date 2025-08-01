# Generated by Django 5.2.4 on 2025-07-22 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_app_enabled"),
    ]

    operations = [
        migrations.CreateModel(
            name="App_Run",
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
                ("Running", models.IntegerField(default=0)),
                ("Active", models.IntegerField(default=0)),
                ("Total", models.IntegerField(default=0)),
                (
                    "app",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.app"
                    ),
                ),
            ],
        ),
    ]
