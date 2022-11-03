from django.db import models


class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def serialize(self):
        return {
            'name': self.name,
            'url': self.url,
            'icon': self.icon
        }
