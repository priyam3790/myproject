# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Employee(models.Model):
    grades = models.CharField(max_length=400)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=1000)
    owner = models.ForeignKey('auth.User', related_name='Emp', on_delete=models.CASCADE)
    email = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("emp:details", kwargs={"name": self.first_name})
