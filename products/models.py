from django.db import models
from django.forms import model_to_dict


class Category(models.Model):
    STATUS_CHOICES = (  # new
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive")
    )

    name = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=100,
        verbose_name="Status of the category",
    )

    class Meta:
        # Table's name
        db_table = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (  # new
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive")
    )

    name = models.CharField(max_length=256)
    #image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=256)

    color = models.CharField(max_length=256, default="Red")
    size = models.TextField(default=0)
    weight=models.FloatField(default=0)

    room = models.CharField(max_length=10,default=0)
    walldirection = models.CharField(max_length=3,default="E")
    column = models.CharField(max_length=10,default=0)
    row = models.CharField(max_length=10,default=0)
    
    
    validity = models.CharField(max_length=20,default=0)

    price = models.FloatField(default=0) 
    currentstock = models.FloatField(default=0)
    stockreminder=models.FloatField(default=0)
    grade=models.CharField(max_length=30,default="empty")
    origin=models.CharField(max_length=30,default="empty")
    


    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=100,
        verbose_name="Status of the product",
    )

    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE, db_column='category')

    
    class Meta:
        # Table's name
        db_table = "Product"

    def __str__(self) -> str:
        return self.name

    def to_json(self):
        item = model_to_dict(self)
        item['id'] = self.id
        item['text'] = self.name
        item['description']=self.description
        item['color']=self.color
        item['size']=self.size
        item['room']=self.room
        item['walldirecion']=self.walldirection
        item['column']=self.column
        item['row']=self.row
        item['validity']=self.validity
        item['price']=self.price
        item['currentstock'] = self.currentstock
        item['stockreminder'] = self.stockreminder
        item['grade'] = self.grade
        item['origin']=self.origin
        item['weight']=self.weight
        item['category'] = self.category.name

        return item
