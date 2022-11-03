from django.db import models


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def serialize(self):
        return {
            'name': self.name,
            'value': self.value
        }
