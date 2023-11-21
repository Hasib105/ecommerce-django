from django.db import models
from django.utils.text import slugify
# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    category_image = models.ImageField(upload_to='category_image', blank=True, null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate unique slug based on the name field
        self.slug = slugify(self.name)

        # Check if the generated slug is unique, if not, append a counter
        counter = 1
        while Category.objects.filter(slug=self.slug).exists():
            self.slug = f"{slugify(self.name)}-{counter}"
            counter += 1

        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    brand_image = models.ImageField(upload_to='brand_image', blank=True, null=True)

    def __str__(self):
        return self.name
    

    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    product_image = models.ImageField(upload_to='product_image', blank=True,null=True)
    description = models.TextField(blank=True)
    summary = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']), 
        ]

    def __str__(self):
        return self.name





        
