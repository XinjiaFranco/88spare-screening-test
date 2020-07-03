from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import CurrencyData
from .serializers import CurrencyDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

@api_view(['GET', 'POST'])
def currency_list(request):
    if request.method == 'GET':
        currencies = CurrencyData.objects.all()
        serializer = CurrencyDataSerializer(currencies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CurrencyDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def currency_detail(request, pk):
    try:
        currency = CurrencyData.objects.get(pk=pk)

    except CurrencyData.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CurrencyDataSerializer(currency)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CurrencyDataSerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        currency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
