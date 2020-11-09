from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
import cloudinary
from cloudinary.models import CloudinaryField



    
    
class Neighbourhood(models.Model):
    user = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=60, null=True)
    description=models.CharField(max_length=400, null=True)
    location=models.CharField(max_length=200, null=True)
    population=models.IntegerField()
    image = CloudinaryField( null = True, blank = True)

    def __str__(self):
        return self.name

    def create_neigbourhood(self):
        self.save()

    def delete_neigbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls,id):
        neighbourhood = cls.objects.get(id=id)
        return neighbourhood

    def update_neighbourhood(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=254, blank=True)
    image =CloudinaryField(default='default.jpg')
    hood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='users', blank=True)
    
    def __str__(self):
        return f'{self.user.username} profile'
    
    


class Business(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=60, null=True)
    description=models.CharField(max_length=400, null=True)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email=models.EmailField()
    image =CloudinaryField(default='default.jpg')

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


class Post(models.Model):
    title = models.CharField(max_length=40)
    post_description = models.CharField(max_length=50)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey('Neighbourhood',on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    image= CloudinaryField(default='default.jpg')

    def __str__(self):
        return self.name

    def save_post(self):
        self.save

    def delete_post(self):
        self.delete
