from django.db import models
from ckeditor.fields import RichTextField


class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = RichTextField(default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    
    def __str__(self):
        return str(self.id)+"-- "+str(self.name)


class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    logo=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)+"-- "+str(self.bank_name)
    

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)+"-- "+str(self.name)
    
    
class LoanEnquiry(models.Model):
    id = models.AutoField(primary_key=True)
    loan = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    candidate = models.CharField(max_length=100)
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    amount = models.CharField(max_length=15)
    tenure = models.CharField(max_length=15)
    adhar=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    pan=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    status=models.CharField(max_length=100,default='Pending')
    
    
    def __str__(self):
        return str(self.id)+"-- "+str(self.name)