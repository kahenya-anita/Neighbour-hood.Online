from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField


# String values are specified as --> Charfield .
# DateTimeField --> Lets THe user know when a specific Item was loaded.
# Null = True --> Allows us to make changes into our database, 
# Allows to import customer with maybe just a name and no phone or email or date created. 
# If null is not set to true There will be an error and we will be forced to add a defult value.
class Hood(models.Model):
    image_1 = CloudinaryField('image')
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

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()


class Profile(models.Model):
    name = models.CharField(max_length=60, null=True)
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
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=60, null=True)
    description=models.CharField(max_length=400, null=True)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email=models.EmailField()
    image = CloudinaryField( null = True, blank = True)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


class Post(models.Model):
    post=models.CharField(max_length=200)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    image= CloudinaryField(default='default.jpg')

    def __str__(self):
        return self.post

    def save_post(self):
        self.save

    def delete_post(self):
        self.delete
