from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404

# Create your views here.

# ----------------------------Non-Primary Key Based Operation ---------------------------

class EmployeeListView(APIView):
    
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
        
        
        
# ----------------------------Primary Key Based Operation ---------------------------


class EmployeeDetailView(APIView):
    
    def get_employee(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
             raise Http404
        
    def get(self, request, pk):
            employee = self.get_employee(pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        
    def delete(self, request , pk):
            self.get_employee(pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def put(self, request , pk):
                employee = self.get_employee(pk)
                serializer = EmployeeSerializer(employee,data=request.data)
                if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data , status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors)
