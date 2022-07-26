from tkinter import EW
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import EmployeeS
import io
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import (
    ListAPIView,
)

class DATA(ListAPIView):
     serializer_class = EmployeeS
     def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset