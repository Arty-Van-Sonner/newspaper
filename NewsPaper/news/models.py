from django.db import models
from accounts.models import NaturalPersons, Accounts

# Create your models here.
class Authors(models.Model):
    account = models.ForeignKey(Accounts, on_delete = models.CASCADE)

class News(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
