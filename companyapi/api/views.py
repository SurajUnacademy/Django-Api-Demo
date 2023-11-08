from django.shortcuts import render
from rest_framework import viewsets 
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # /companies/{companyId}/employees
    @action(detail = True, methods = ['get'])     # this annotation helps to run this Api in which pk will be used to run this custom api
    def employees(self, request, pk = None):      # detail true means that we must pass the pk while api calling and As it is made under comanyViewSet then this 
        try:
            company = Company.objects.get(pk = pk)    # this will be run using /companies url. this pk ( must) then employees.
            emps = Employee.objects.filter(company = company) #now these employees will be send as serialized one as we need send it in json
            emps_serializer = EmployeeSerializer(emps, many = True, context = {'request' : request})   #( data = emps, many referred to many objects of emp, context refers request )
            return Response(emps_serializer.data)    # serialized response will be sent
        except Exception as e:
            print(e)
            return Response({
                'message' : 'Company might not exists !! Error'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer