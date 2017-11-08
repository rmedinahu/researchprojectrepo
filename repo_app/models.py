# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    thefile = models.FileField(upload_to='uploads/')

class Category(models.Model):
    label = models.CharField(max_length=255)


class Project(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()

class Task(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    order = models.IntegerField(default=0)
    project = models.ForeignKey(Project)
    category = models.ForeignKey(Category) # required
    assignee = models.ForeignKey(User, null=True) # optional

class Metadata(models.Model):
    descriptor = models.CharField(max_length=512)
    data = models.TextField()
    project = models.ForeignKey(Project)


class Membership(models.Model):
    member = models.ForeignKey(User)
    project = models.ForeignKey(Project, related_name='prj_membership')
    is_owner = models.BooleanField(default=False)
    

class TaskFile(models.Model):
    task = models.ForeignKey(Task)
    file = models.ForeignKey(File)















