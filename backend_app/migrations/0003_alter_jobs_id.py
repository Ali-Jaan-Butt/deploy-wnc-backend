# Generated by Django 5.1.3 on 2024-11-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend_app", "0002_rename_job_id_proposal_job_id_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]