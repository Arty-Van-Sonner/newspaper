from django.db import models


class School(models.Model):

   name = models.CharField(max_length=64, unique=True)
   address = models.CharField(max_length=120)
   is_active = models.BooleanField(default=True)


class SClass(models.Model):
   grade = models.IntegerField()
   school = models.ForeignKey(School, on_delete=models.CASCADE)


class Student(models.Model):
   name = models.CharField(max_length=64)
   sclass = models.ForeignKey(SClass, on_delete=models.CASCADE)