from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150, null=True)
    sub_title = models.CharField(max_length=150, null=True)
    content = models.TextField(null=True)
    ratings = models.FloatField(null=True)
    date_posted = models.DateField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)
    author = models.CharField(max_length=50,null=True)
    image = models.ImageField(null= True)

    def __str__(self):
        return self.title
