from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Company
from .serializers import CompanySerializer
from django.http import Http404

# Create your views here.

class CompanyListView(APIView):
    
    def get(self,request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies , many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        

class CompanyDetailView(APIView):
    
    def get_company(self,pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist :
            return Http404
    def get(self,request,pk):
        company = self.get_company(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    def delete(self, request , pk):
            self.get_company(pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        company = self.get_company(pk)
        serializer = CompanySerializer( company , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors) 