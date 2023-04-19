from django.db import models
from companyctlg.models import Company, Ourfirm


def ourfirm_default():
    return 1


class Receipt(models.Model):
    number = models.CharField(max_length=9, blank=False)
    datetime = models.DateTimeField(blank=False)
    ourfirm = models.ForeignKey(Ourfirm, on_delete=models.RESTRICT, default=ourfirm_default)
    company = models.ForeignKey(Company, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return f'N:{self.number} D:{self.datetime.strftime("%d-%m-%Y %H:%M:%S")} ({self.company.name})'


class Shipment(models.Model):
    number = models.CharField(max_length=9, blank=False)
    datetime = models.DateTimeField(blank=False)
    ourfirm = models.ForeignKey(Ourfirm, on_delete=models.RESTRICT, default=ourfirm_default)
    company = models.ForeignKey(Company, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return f'N:{self.number} D:{self.datetime.strftime("%d-%m-%Y %H:%M:%S")} ({self.company.name})'

