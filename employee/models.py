from django.db import models
from django.contrib.auth.models import User

class employee(models.Model):
    #user= models.OneToOneField(User, on_delete=models.CASCADE)
    employeeid = models.IntegerField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=25,null=True)
    image= models.ImageField(null=True, upload_to='images/', default='images/None/no-img', blank=True)
     
    def __str__(self):
        return self.firstname

