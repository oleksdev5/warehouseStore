from django.db import models

class ThingFolder(models.Model):
    name = models.CharField(max_length=70)
    folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Thing(models.Model):
    name = models.CharField(max_length=150)
    folder = models.ForeignKey(ThingFolder, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.folder})'
