from django.db import models


class Customer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=500)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def Already_Exists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
        

   

