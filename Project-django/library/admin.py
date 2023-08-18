from django.contrib import admin
from .models import Customer,Book,Loan

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Loan)