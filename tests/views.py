from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def fibonnaci(request, number, format=None):
    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    fibo = fib(int(number))
    return Response(fibo)


@api_view(['GET'])
def hello(request, format=None):
    return Response('Hello world')

