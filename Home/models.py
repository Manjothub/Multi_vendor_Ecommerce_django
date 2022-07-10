from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

class FrontSlider(models.Model):
    Deals =(
        ('Hot Deals','Hot Deals'),
        ('New Arraivals','New Arraivals')
    )
    
    image = models.ImageField(upload_to='media/slider-img')
    discount_deal = models.CharField(choices=Deals,max_length=100)
    Sale = models.IntegerField()
    brand_name = models.CharField(max_length = 200)
    discount = models.IntegerField()
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.brand_name
    
class MainCategory(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    main_category = models.ForeignKey(MainCategory,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + " --- " + self.main_category.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category.main_category.name + " ---" + self.category.name + "---" + self.name 
    
class Section(models.Model):
    name = models.CharField(max_length =100)
    
    def __str__(self):
        return self.name

class Color(models.Model):
    code = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.code

class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name




class Product(models.Model):
    total_quantity = models.IntegerField()
    availability = models.IntegerField()
    feature_img = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    Product_information = RichTextField(null=True)   
    categories = models.ForeignKey(Category,on_delete= models.CASCADE)
    color = models.ForeignKey(Color,on_delete = models.CASCADE, null= True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    tags = models.CharField(max_length=100)
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    Description = RichTextField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    
    def __str__(self): 
        return self.product_name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "Home_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)

    

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)


class AdditionalInformation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    
