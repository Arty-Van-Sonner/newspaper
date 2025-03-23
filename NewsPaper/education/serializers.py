from .models import *
from rest_framework import serializers


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = School
       fields = ['id', 'name', ]


class SClassSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = SClass
       fields = ['id', 'grade', ]


class StudentSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Student
       fields = ['id', 'name', ]