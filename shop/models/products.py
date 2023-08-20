from django.db import models
from .category import Category

class Products(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='uploads/products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=0)


    @staticmethod
    def get_all_products():
       return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryId(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)



