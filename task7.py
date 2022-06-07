from django.db import models

class Product(models.Model):
    Product_Name = models.CharField(max_length=10000)
    Product_Price = models.CharField(max_length=10000)

    def __str__(self):
        return self.Product_Name


# Inserting a new record into the product model
x = Product(Product_Name = 'toy', Product_Price = '$30')
x.save()

# Getting all the records in the product table
all_records = Product.objects.all()
all_records

# Filtering products by name
Product.objects.filter(Product_Name = 'egg')

# Getting a product price
Product.objects.filter(Product_Price = '$80')

# Changing a product price
Product.objects.filter(Product_Price = '$80')
x = Product(Product_Price = '£80')
x.save()