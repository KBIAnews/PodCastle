# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sponsor (models.Model):
    slug = models.SlugField(max_length=250,
                            unique=True)
    name = models.CharField(max_length=512)
    link_url = models.URLField(max_length=2048)
    logo = models.ImageField()
