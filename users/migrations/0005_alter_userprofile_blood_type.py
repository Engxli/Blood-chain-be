# Generated by Django 3.2.13 on 2022-06-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_userprofile_blood_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="blood_type",
            field=models.CharField(
                choices=[
                    ("A-", "Amin"),
                    ("A+", "Apos"),
                    ("O-", "Omin"),
                    ("O+", "Opos"),
                    ("B-", "Bmin"),
                    ("B+", "Bpos"),
                    ("AB-", "Abmin"),
                    ("AB+", "Abpos"),
                ],
                max_length=3,
                null=True,
            ),
        ),
    ]
