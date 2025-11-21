from django.db import models


class Mobile(models.Model):
    mobile_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=3)
    password =models.CharField(max_length=10) 

    
class Admin(models.Model):
    username = models.CharField(max_length=20)
    password =models.CharField(max_length=10) 
        
    
    
    


