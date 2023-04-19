from django.db import models

def uom_code_default():
    return "000"


class UoM(models.Model):
    code = models.CharField(primary_key=True, max_length=3, default=uom_code_default)
    name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.name


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
