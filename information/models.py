from django.db import models

# Create your models here.

class People(models.Model):
    First_Name = models.CharField(max_length=10000)
    Last_Name = models.CharField(max_length=10000)
    Username = models.CharField(max_length=10000)

    def __str__(self):
        return self.Username

class Address(models.Model):
    Home_Address = models.CharField(max_length=10000)
    Vacation_Address = models.CharField(max_length=10000)
    User = models.ForeignKey(People, on_delete=models.CASCADE)

class Doctor(models.Model):
    First_Name = models.CharField(max_length=10000)
    Last_Name = models.CharField(max_length=10000)
    Name_Of_Patient = models.ManyToManyField(People)

    def __str__(self):
        return self.Last_Name

class Bio(models.Model):
    Add_Bio = models.CharField(max_length=10000, default='')
    About = models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.About

class Product(models.Model):
    Product_Name = models.CharField(max_length=10000)
    Product_Price = models.CharField(max_length=10000)

    def __str__(self):
        return self.Product_Name

