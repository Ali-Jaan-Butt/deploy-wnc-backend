# Generated by Django 5.1.3 on 2024-11-20 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="proposal",
            old_name="job_id",
            new_name="job_id_id",
        ),
    ]
