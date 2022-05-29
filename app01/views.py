from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .ser import BookModelSerializer


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class Books(View):
    def get(self, request):
        return HttpResponse('ok')
