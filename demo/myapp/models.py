# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class task_record(models.Model):
    status=models.CharField(verbose_name='状态',max_length=1)
    create_At=models.DateTimeField(auto_now=True)
    update_At=models.DateTimeField(auto_now=True)
