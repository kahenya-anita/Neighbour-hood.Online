from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

import cloudinary
from cloudinary.models import CloudinaryField


class Hood(models.Model):
    image_1 = CloudinaryField('image')
    image_2 = CloudinaryField('image')
    image_3 = CloudinaryField('image')
    
    
class Neighbourhood(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=60, null=True)
    description=models.CharField(max_length=400, null=True)
    location=models.CharField(max_length=200, null=True)
    population=models.IntegerField()
    image = CloudinaryField( null = True, blank = True)
    hoods = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='neighbourhood_images')

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
    name = models.CharField(max_length=60, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, null=True)
    hood = models.ForeignKey('Neighbourhood', max_length=200, on_delete=models.CASCADE, null=True)
    image = CloudinaryField(default='default.jpg')

    def __str__(self):
        return self.name

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=60, null=True)
    description=models.CharField(max_length=400, null=True)
    neighbourhood=models.ForeignKey('Neighbourhood' ,on_delete=models.CASCADE)
    email=models.EmailField()
    image = CloudinaryField( null = True, blank = True)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()
        
    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id=business_id)
        return business

    def update_business(self,name):
        self.name = name
        self.save()


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
