from django.db import models

# Create your models here.
#新增VIP的MODEL
class VipInfodata(models.Model):
    cname=models.CharField(max_length=50,null=False)
    cemail=models.EmailField(max_length=50,null=False)
    cpasswd=models.CharField(max_length=50,null=False)
    cphone=models.CharField(max_length=50,null=False)
    cBirthday=models.DateField(null=True)
    cAddr=models.CharField(max_length=50,null=True)