from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)                                        
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name
#class Meta:
   # ordering = ('name',)
    #verbose_name = 'category'
   # verbose_name_plural = 'categories'
    
class SubCategory(models.Model):
    name = models.CharField(max_length=200,db_index=True)                                        
    state = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

#class Meta:
  #  ordering = ('name',)
  #  verbose_name = 'subcategory'
  #  verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,blank=True,default=None,on_delete=models.CASCADE)
    subcategory = models.OneToOneField(SubCategory,unique=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    #related_name='products',on_delete=models.CASCADE)
    #slug = models.SlugField(max_length=200, db_index=True)
    #description = models.TextField(blank=True)

#class Meta:
   # ordering = ('name',)
    #index_together = (('id', 'slug'),)
    