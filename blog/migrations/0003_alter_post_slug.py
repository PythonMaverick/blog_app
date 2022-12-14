# Generated by Django 4.1.2 on 2022-10-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_author_alter_post_publish_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
