from django.db import models

# Create your models here.

class Store_list (models.Model):
    name = models.CharField (max_length=50)
    location = models.CharField (max_length=100)
    website = models.URLField (max_length=50)

    def __str__(self):
        return self.name
    
class Pant_list (models.Model):
    name = models.CharField (max_length=50)
    desc = models.CharField (max_length=100)
    store = models.ForeignKey (Store_list , on_delete=models.CASCADE , related_name="store_list" , null=True)
 
    def __str__(self):
        return self.name
    

    
