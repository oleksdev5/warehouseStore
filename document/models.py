from django.db import models
from companyctlg.models import Company, Ourfirm
from thingctlg.models import Thing, UoM


def ourfirm_default():
    return 1


class Receipt(models.Model):
    number = models.CharField(max_length=9, blank=False)
    datetime = models.DateTimeField(blank=False)
    ourfirm = models.ForeignKey(Ourfirm, on_delete=models.RESTRICT, default=ourfirm_default)
    company = models.ForeignKey(Company, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return f'N:{self.number} D:{self.datetime.strftime("%d-%m-%Y %H:%M:%S")}, {self.company.name}'


class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.RESTRICT)
    thing = models.ForeignKey(Thing, on_delete=models.RESTRICT, verbose_name='Material')
    uom = models.ForeignKey(UoM, on_delete=models.RESTRICT, verbose_name='UoM')
    quantity = models.DecimalField(max_digits=13, decimal_places=4)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{thing.name}, {quantity}{uom.name}, ${price}, (shipment: {receipt})'

    class Meta:
        unique_together = ['receipt', 'thing']

class Shipment(models.Model):
    number = models.CharField(max_length=9, blank=False)
    datetime = models.DateTimeField(blank=False)
    ourfirm = models.ForeignKey(Ourfirm, on_delete=models.RESTRICT, default=ourfirm_default)
    company = models.ForeignKey(Company, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return f'N:{self.number} D:{self.datetime.strftime("%d-%m-%Y %H:%M:%S")}, {self.company.name}'


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.RESTRICT)
    thing = models.ForeignKey(Thing, on_delete=models.RESTRICT, verbose_name='Product')
    uom = models.ForeignKey(UoM, on_delete=models.RESTRICT, verbose_name='UoM')
    quantity = models.DecimalField(max_digits=13, decimal_places=4)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{thing.name}, {quantity}{uom.name}, S{price}, (shipment: {shipment})'

    class Meta:
        unique_together = ['shipment', 'thing']