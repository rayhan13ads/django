# Generated by Django 2.0.7 on 2018-09-08 12:23

from django.db import migrations, models
import newsApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0003_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=newsApp.models.upload_path),
        ),
    ]
