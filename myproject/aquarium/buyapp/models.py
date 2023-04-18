from django.db import models
class Register(models.Model):
    phone=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    passwd=models.CharField(max_length=50,null=False)

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    EDUCATION_CHOICES = (
        ('', 'Please select'),
        ('H', 'High school or below'),
        ('C', 'College'),
        ('G', 'Graduate school'),
    )
    education = models.CharField(max_length=1, choices=EDUCATION_CHOICES)






class Purchase(models.Model):   
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    shipping_status = models.CharField(max_length=20)
    # ?��以�?��?��?��?��??�?費相??��??�?�?


class PaymentInfo(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    # ??��?�可以�?��?��?��?��??付款?��??��??�?�?

class ShoppingCart(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name