# Generated by Django 5.1.3 on 2024-12-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend_app", "0010_alter_place_orders_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place_orders",
            name="end_date",
            field=models.TextField(),
        ),
    ]