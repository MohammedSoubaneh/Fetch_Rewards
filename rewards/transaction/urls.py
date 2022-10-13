from django.urls import path
from .views import ListTransactions, SpendPoints

urlpatterns = [
    path('', ListTransactions.as_view(), name='list_transaction'),
    path('send-transaction', ListTransactions.as_view(), name='send_transaction'),
    path('spend-points', SpendPoints.as_view(), name="spend_points"),
]