from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    display_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
        
    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_weight = models.BooleanField(default=False, null=True, blank=True)
    sku = models.CharField(max_length=250, null=True, blank=True)
    image_url= models.URLField(null=True, blank=True, max_length=1024)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name