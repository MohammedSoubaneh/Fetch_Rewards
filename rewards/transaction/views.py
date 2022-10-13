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

class GetBalance(APIView):

    def get(self, request, format=None):
        pass

class SpendPoints(APIView):

    def spend_points(self, points, pk=1):
        get_points = Transaction.objects.get(pk=pk)
        points_spent: int = points
        if int(points_spent) > get_points.points:
            if Transaction.objects.filter(pk=pk+1).exists():
                points_spent = int(points_spent) - get_points.points
                get_points.points = 0
                get_points.save()
                return SpendPoints.spend_points(self, points=points_spent, pk=pk+1)
            serializer = TransactionSerializer(get_points)
            return Response(serializer.data)
        get_points.points -= int(points_spent)
        get_points.save()
        serializer = TransactionSerializer(get_points)
        return Response(serializer.data)


    def post(self, request, format=None):
        point_spent = request.data["points"]
        return self.spend_points(point_spent)