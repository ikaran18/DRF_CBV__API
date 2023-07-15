from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

#  ---------------- Non-Primary Key Based Opeartions -----------------------

class BookListView(APIView):
    
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books , many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
#  ----------------Primary Key Based Opeartions -----------------------


class BookDetailView(APIView):
    
    def get_book(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Http404

    def get(self,request,pk):
        book = self.get_book(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def delete(self,request,pk):
        self.get_book(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        book = self.get_book(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
