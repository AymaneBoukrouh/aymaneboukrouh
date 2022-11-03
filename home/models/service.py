from django.db import models


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def serialize(self):
        return {
            'title': self.title
        }

    def __str__(self):
        return self.title
