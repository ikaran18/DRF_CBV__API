from django.urls import path
from .views import *

urlpatterns = [
    path('',CompanyListView.as_view()),
    path('company/<int:pk>',CompanyDetailView.as_view()),
]
