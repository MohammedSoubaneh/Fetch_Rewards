from django.urls import path
from .views import ListTransactions

urlpatterns = [
    path('', ListTransactions.as_view(), name='list_transaction'),
    path('send-transaction', ListTransactions.as_view(), name='send_transaction')
]