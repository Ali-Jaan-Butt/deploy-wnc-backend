# Generated by Django 5.1.3 on 2024-12-10 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend_app", "0006_alter_place_orders_end_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="place_orders",
            old_name="job_id_id",
            new_name="job_id_id_id",
        ),
    ]