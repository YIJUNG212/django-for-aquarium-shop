from django.db import models

# Create your models here.
#增加一個正式用的資料表
class VipInfodata(models.Model):
    cname=models.CharField(max_length=50,null=False)
    cemail=models.EmailField(max_length=50,null=False)
    cpasswd=models.CharField(max_length=50,null=False)
    cphone=models.CharField(max_length=50,null=False)
    cBirthday=models.DateField(null=True)
    cAddr=models.CharField(max_length=50,null=True)