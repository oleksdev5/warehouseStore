from django.db import models


# def company_default():
#     return 1


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Ourfirm(models.Model):
    company = models.OneToOneField(Company, primary_key=True, on_delete=models.RESTRICT)

    def __str__(self):
        return self.company.name


class Agreement(models.Model):
    number = models.CharField(max_length=25, blank=False)
    date = models.DateField(blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.number} {self.date.strftime("%d-%m-%Y")} ({self.company.name})'
