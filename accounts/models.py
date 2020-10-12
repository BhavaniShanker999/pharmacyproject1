from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True,)
    phone = models.IntegerField( null=True,)
    email = models.EmailField(max_length=50, null=True,)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(('Emergency','Emergency'),('Demanded','Demanded'))
    name=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=500,null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    price=models.FloatField()
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('Delivered','Delivered'),('Out For Delivery','Out For Delivery'),
              ('Out Of Stock','Out Of Stock'),('Not Available','Not Available'))

    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity=models.IntegerField()
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


