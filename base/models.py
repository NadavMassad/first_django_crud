from django.db import models

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.sName

        
class Phones(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.sName
