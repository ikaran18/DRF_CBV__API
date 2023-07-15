from django.urls import path
from .views import *

urlpatterns = [
    path('',EmployeeListView.as_view()),
    path('employee/<int:pk>',EmployeeDetailView.as_view()),
    
]
