from django.contrib.auth.models import User
from django.db import models

# Create your models here.
PLACE_CHOICES=(
     ('KL','Kerala'),
     ('KR','Karnataka'),
     ('AP','Andrapradesh'),
     ('GO','Goa'),
     ('ND','Newdelhi'),
     ('UT','Utterpradesh'),
     ('GR','Greece'),
     ('FR','France'),
     ('ID','Indonesia'),
)

class Places(models.Model):
     title=models.CharField(max_length=250)
     price=models.IntegerField()
     offerprice=models.IntegerField()
     description=models.TextField()
     place=models.CharField(choices=PLACE_CHOICES,max_length=3)
     image=models.ImageField(upload_to='places')

     def __str__(self):
         return self.title


class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    Address=models.TextField(default=0)
    dateofbirth=models.IntegerField()
    Requirements=models.CharField(max_length=100)


class Payment(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)


