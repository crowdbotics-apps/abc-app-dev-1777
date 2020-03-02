from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    a1 = models.BigIntegerField(null=True, blank=True,)
    a2 = models.BigIntegerField(null=True, blank=True,)
    a3 = models.BigIntegerField(null=True, blank=True,)
    a4 = models.BigIntegerField(null=True, blank=True,)
    a5 = models.BigIntegerField(null=True, blank=True,)
    a6 = models.BigIntegerField(null=True, blank=True,)
    a7 = models.BigIntegerField(null=True, blank=True,)
    a8 = models.BigIntegerField(null=True, blank=True,)
    a9 = models.BigIntegerField(null=True, blank=True,)
    a10 = models.BigIntegerField(null=True, blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
