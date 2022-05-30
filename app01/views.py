from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .ser import BookModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class Books(View):
    def get(self, request):
        print(self.request)
        return HttpResponse('ok')


class BooksAPIView(APIView):
    def get(self, request):
        print(request.data)
        return HttpResponse('ok')
