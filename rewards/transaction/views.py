from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Transaction
from rest_framework.response import Response
from .serializer import TransactionSerializer

class ListTransactions(APIView):

    def get(self, request, format=None):
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    