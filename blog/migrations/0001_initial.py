# Generated by Django 4.1.2 on 2022-10-21 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=250)),
                ("slug", models.CharField(max_length=250)),
                ("body", models.TextField()),
                (
                    "publish",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2022,
                            10,
                            21,
                            22,
                            30,
                            29,
                            64164,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Published")],
                        default="DF",
                        max_length=2,
                    ),
                ),
            ],
            options={"ordering": ["-publish"],},
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["-publish"], name="blog_post_publish_bb7600_idx"
            ),
        ),
    ]
