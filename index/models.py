from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=550)
    category_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=880)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_photo = models.ImageField()
    product_quantity = models.IntegerField(blank=True, null=True)
    product_date = models.DateTimeField(auto_now_add=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()

    def __str__(self):
        return str(self.user_id)