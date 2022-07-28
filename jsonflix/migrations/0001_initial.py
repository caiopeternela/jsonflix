# Generated by Django 4.0.6 on 2022-07-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('show_id', models.CharField(max_length=36, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(max_length=36)),
                ('title', models.CharField(max_length=512)),
                ('director', models.CharField(blank=True, max_length=512, null=True)),
                ('cast', models.TextField()),
                ('country', models.CharField(max_length=512)),
                ('date_added', models.CharField(max_length=36)),
                ('release_year', models.CharField(max_length=36)),
                ('rating', models.CharField(max_length=36)),
                ('duration', models.CharField(max_length=64)),
                ('genres', models.CharField(max_length=512)),
                ('description', models.TextField()),
            ],
        ),
    ]