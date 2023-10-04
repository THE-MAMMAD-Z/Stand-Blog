from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    child='child'
    teen='teen'
    adult='adult'
    
    AGE_FIELDS=(
        (child,'child'),(teen,'teen'),(adult,'adult')
    )
    
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=False)
    age=models.CharField(max_length=255,default=adult,choices=AGE_FIELDS)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category=models.ManyToManyField("Category")
    image=models.ImageField(upload_to='blog/',null=True,default='blog/sport.jpg')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering=['-updated_time']
        
class Description(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50,null=True)
    message=models.TextField(blank=True)
    
    def __str__(self):
        return self.subject
    
class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    Active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-created_time']
    
    
    
        
            

