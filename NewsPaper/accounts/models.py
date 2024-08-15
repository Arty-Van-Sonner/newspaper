from django.db import models

director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

# Create your models here.
class NaturalPersons(models.Model):
    first_name = models.CharField(max_length = 128)
    surname = models.CharField(max_length = 128)
    main_email = models.EmailField()

class Accounts(models.Model):
    natural_person = models.ForeignKey(NaturalPersons, on_delete = models.CASCADE)
    creation_date = models.DateField(auto_now_add = True)
    date_of_last_update = models.DateField(auto_now = True)
    nick = models.CharField(max_length = 255)
    password = models.TimeField()

class Staff(models.Model):
    natural_person = models.ForeignKey(NaturalPersons, on_delete = models.CASCADE)
    position = models.CharField(max_length = 2, choices = POSITIONS, default = cashier)
    # labor_contract = 