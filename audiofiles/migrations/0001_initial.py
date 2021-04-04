# Generated by Django 3.1.7 on 2021-04-01 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2021, 4, 1, 20, 53, 47, 206553))),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2021, 4, 1, 20, 53, 47, 206553))),
                ('host', models.CharField(max_length=100)),
                ('participants', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2021, 4, 1, 20, 53, 47, 206553))),
            ],
        ),
    ]