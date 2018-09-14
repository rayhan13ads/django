# Generated by Django 2.0.7 on 2018-09-09 23:12

import civilized_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_name', models.FileField(blank=True, null=True, upload_to=civilized_app.models.upload_path)),
            ],
        ),
    ]
