# Generated by Django 2.0.7 on 2018-09-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descirption', models.TextField()),
            ],
            options={
                'verbose_name': 'BlogModel',
                'verbose_name_plural': 'BlogModels',
            },
        ),
    ]
