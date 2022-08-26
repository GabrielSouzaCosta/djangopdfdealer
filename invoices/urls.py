from django.urls import path

from invoices.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
]
