from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    def __str__(self):
        return self.user.username


class Product(models.Model):
    # product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    artby = models.CharField(max_length=20,default="")
    # category = models.CharField(max_length=50,default="")
    # subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=500)
    # pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
    
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    # items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")

    def __str__(self):
        return self.email
    
class UpdateOrder(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000, default="")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
class Contact(models.Model):
    name = models.CharField(max_length=20, default="")
    email= models.CharField(max_length=50, default="")
    phone= models.CharField(max_length=12, default="")
    rqst= models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.email
