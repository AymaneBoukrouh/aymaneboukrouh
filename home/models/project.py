from django.db import models
from home.models.technology import Technology


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    @property
    def technologies(self):
        return [pt.technology.name for pt in ProjectTechnology.objects.filter(project=self)]

    @property
    def links(self):
        return [pl.serialize() for pl in ProjectLink.objects.filter(project=self)]
    
    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'technologies': self.technologies,
            'links': self.links
        }

    def __str__(self):
        return self.title


class ProjectTechnology(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.title} - {self.technology.name}"


class ProjectLink(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.project.title} - {self.icon}"

    def serialize(self):
        return {
            'url': self.url,
            'icon': self.icon
        }
