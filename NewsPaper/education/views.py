from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from education.serializers import *
from education.models import *


class SchoolViewset(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = SchoolSerializer

   def list(self, request, format=None):
       return Response([])


class SClassViewset(viewsets.ModelViewSet):
   queryset = SClass.objects.all()
   serializer_class = SClassSerializer
   filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
   filterset_fields = ["grade", "school_id"]


class StudentViewest(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   permission_classes = [permissions.IsAuthenticated]
   
   def get_queryset(self):
       queryset = Student.objects.all()
       school_id = self.request.query_params.get('school_id', None)
       sclass_id = self.request.query_params.get('sclass_id', None)
       if school_id is not None:
           queryset = queryset.filter(sclass__school_id=school_id)
       if sclass_id is not None:
           queryset = queryset.filter(sclass_id=sclass_id)
       return queryset