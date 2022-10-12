from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)

class TransactionModel(admin.ModelAdmin):
    list_display = ['payer']