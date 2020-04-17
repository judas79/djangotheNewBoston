# from django.shortcuts import render
'''
# L40 return a 404 if the object doesn't exist
from django.shortcuts import get_object_or_404

# makes normal views return API data
from rest_framework.views import APIView

# response works with status to return a response which will be JSON
from rest_framework.response import Response
from rest_framework import status

# import the fields from the class Stock in models.py
from .models import Stock

# convert class model into JSON for saving to a HD or sending over a network
# StockSerializer was created from our Stock class in models.py, and StockSerializer resides in serializer.py
from .serializer import StockSerializer
'''
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

# Create your views here.

# handle get and post requests, from API;  get all info in database, or
# user creates a new stock, into the data base
# stocks/
class StockList(APIView):

    def get(self, request):

        # create variable, get everything to send in the list
        stocks = Stock.objects.all()

        # turn it into JSON using serializer, 1st parameter is what you are sending
        # second parameter is it many or just one
        serializer = StockSerializer(stocks, many=True)

        # make HTTP able to send JSON data
        return Response(serializer.data)


    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)