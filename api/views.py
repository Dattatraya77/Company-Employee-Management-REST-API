from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from api.serializers import CompanySerializers, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emps, many=True, context={'request':request})
            if emp_serializer.data:
                return Response(emp_serializer.data)
            else:
                context = {
                    "message": "OOPS, Employee Not Found!"
                }
                return Response(context)
        except Exception as e:
            context = {
                "message": "OOPS, Company Not Found!"
            }
            return Response(context)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
