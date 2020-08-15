from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null= True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null= True)
    price =models.DecimalField(max_digits=10, decimal_places=3)
    digital = models.BooleanField(default=False,null=True,blank=True)
    product_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            URL=  self.product_image.url
        except:
            URL = ""
        return URL
    
    # def delete(self, *args, **kwargs):
    #     self.product_image.delete()
    #     super().delete(*args, **kwargs)


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitem = self.orderitem_set.all()
        for i in orderitem:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_total_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total

    @property
    def get_total_item(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        return self.product.price * self.quantity


class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null= True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    addess = models.CharField(max_length=200, null= True)
    city = models.CharField(null = True, max_length=50)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.addess) < 20:
            return self.addess
        else:
            return self.addess[:20]+"...."







