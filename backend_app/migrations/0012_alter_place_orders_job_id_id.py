# Generated by Django 4.1.3 on 2024-12-18 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("backend_app", "0011_alter_place_orders_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place_orders",
            name="job_id_id",
            field=models.ForeignKey(
                default="None",
                on_delete=django.db.models.deletion.CASCADE,
                to="backend_app.jobs",
                to_field="job_id",
                unique=True,
            ),
        ),
    ]
