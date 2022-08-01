# Generated by Django 4.0.6 on 2022-08-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jsonflix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
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