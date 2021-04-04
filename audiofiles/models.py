from datetime import datetime
from django.utils import timezone
from django.db import models


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    upload_time = models.DateTimeField(default=timezone.now, null=False)


class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    upload_time = models.DateTimeField(default=timezone.now, null=False)
    host = models.CharField(max_length=100, null=False)
    participants = models.TextField(null=True)


class Audiobook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    narrator = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    upload_time = models.DateTimeField(default=timezone.now, null=False)
