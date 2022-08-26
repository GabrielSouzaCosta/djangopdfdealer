from django.db import models
from django.contrib.auth.models import User


def upload_to(self, filename):
    print(filename)
    return f'invoices/{self.owner_name}/{filename}'

class Invoice(models.Model):
    owner_name = models.CharField(max_length=250)
    invoice_file = models.FileField(upload_to=upload_to, null=False, blank=False)
    created_in = models.DateTimeField(auto_now_add=True)
    
    def get_invoice_file(self):
        if self.invoice_file:
            return self.invoice_file.url
        return 'no file'

    def __str__(self):
        return f'Invoice Nº{id}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def get_total_value(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"