from audioop import reverse
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core.files.base import File
from invoices.forms import InvoiceForm
from invoices.models import Invoice, Product

from invoices.scripts import html_to_pdf

def homepage(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            owner = form.cleaned_data['owner_name']
            pdf = html_to_pdf('invoice.html', context_dict={"owner": owner, "items": products})
            file = BytesIO(pdf.content)
            for f in pdf:
                print(f)
            invoice = Invoice.objects.create(owner_name=owner)
            invoice.invoice_file = File(file, 'invoice.pdf')
            invoice.save()
            return HttpResponse(pdf, content_type='application/pdf')

    else:
        form = InvoiceForm()
    return render(request, 'invoices/index.html', {"form": form, "products": products})