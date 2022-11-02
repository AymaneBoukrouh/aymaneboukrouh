from django.db import models


class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
