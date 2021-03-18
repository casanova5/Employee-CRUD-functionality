from django.db import models
from django.urls import reverse,reverse_lazy
# Create your models here.

class employee(models.Model):
    emp_id=models.AutoField(primary_key=True,serialize=False, verbose_name='ID')
    emp_name=models.CharField(max_length=100)
    emp_email=models.EmailField()

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk':self.pk})
    class Meta:  
        db_table = "employee"  
        ordering = ['emp_id',]#sorts the records ascending using 'emp_id' field