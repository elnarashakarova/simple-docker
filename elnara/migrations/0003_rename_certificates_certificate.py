# Generated by Django 5.0.7 on 2024-07-26 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("elnara", "0002_certificates"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Certificates",
            new_name="Certificate",
        ),
    ]
