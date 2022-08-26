from django.test import TestCase, Client
from django.core.files import File
from django.urls import reverse

from invoices.forms import InvoiceForm
from .scripts import html_to_pdf
from io import BytesIO
import json

from invoices.models import Invoice, Product

client = Client()

class CreateInvoiceTest(TestCase):
    def setUp(self):
        invoice = Invoice.objects.create(owner_name='gabriel')
        # Create the pdf process and set it to the object
        pdf = html_to_pdf('invoice.html', context_dict={"owner": 'gabriel'})
        file = BytesIO(pdf.content)
        invoice.invoice_file = File(file, 'invoice.pdf')
        # -----------------------------------------------
        invoice.save()  

    def test_invoice_data(self):
        invoice = Invoice.objects.filter(owner_name='gabriel').first()
        self.assertEqual('gabriel', invoice.owner_name)
        self.assertIn('https://personalprojects-s3bucket.s3.amazonaws.com/invoices/', invoice.get_invoice_file())


class CreateInvoiceViewTest(TestCase):
    def test_create_invoice_with_pdf(self):
        data = {"owner_name": "jose"}
        response = client.post(reverse('homepage'), json.dumps(data), content_type="application/x-www-form-urlencoded") 
        self.assertEqual(response.status_code, 200)
