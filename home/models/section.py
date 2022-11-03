from django.db import models


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def serialize(self):
        return {
            'title': self.title,
            'icon': self.icon
        }
