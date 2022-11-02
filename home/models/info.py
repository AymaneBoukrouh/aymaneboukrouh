from django.db import models


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
