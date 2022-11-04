from django.db import models
from home.models.technology import Technology


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def serialize(self):
        return {
            'name': self.name,
            'value': self.value
        }


class Field(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    @property
    def technologies(self):
        return [ft.technology.name for ft in FieldTechnology.objects.filter(field=self)]
    
    def serialize(self):
        return {
            'name': self.name,
            'technologies': self.technologies
        }


class FieldTechnology(models.Model):
    id = models.AutoField(primary_key=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
