from django.urls import path
from .views import ListTransactions, SpendPoints, GetBalance

urlpatterns = [
    path('', ListTransactions.as_view(), name='list_transaction'),
    path('send-transaction', ListTransactions.as_view(), name='send_transaction'),
    path('spend-points', SpendPoints.as_view(), name="spend_points"),
    path('get_balance', GetBalance.as_view(), name="get_balance"),
]