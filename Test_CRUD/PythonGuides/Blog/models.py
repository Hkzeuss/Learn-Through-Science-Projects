from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Blog(models.Model):
    BlogId = models.CharField(max_length=30)
    Title = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=300)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Content_Blog = HTMLField(blank=True, null=True)
    Image_Blog = models.ImageField(upload_to='blog_images/', default='blog_images/default_image.jpg')
    
    

    class Meta:
        db_table = 'Blog'
        
        
        
        