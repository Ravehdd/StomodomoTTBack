# Generated by Django 4.2.16 on 2024-10-26 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clinic",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("add_time", models.DateTimeField()),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("cancel_time", models.DateTimeField(null=True)),
                ("card_comment", models.CharField(max_length=255, null=True)),
                ("reception_comment", models.CharField(max_length=255, null=True)),
                (
                    "clinic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stoma.clinic"
                    ),
                ),
                (
                    "doctor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stoma.doctor"
                    ),
                ),
            ],
        ),
    ]
