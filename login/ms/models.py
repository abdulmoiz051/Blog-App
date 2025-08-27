from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .utils import create_slug
# Create your models here.

class custom_user(AbstractUser):
    phone_number = models.CharField(max_length=12)
    profile_picture = models.ImageField( upload_to='profile/',null=True,blank=True)




class blog(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='blog/',null=True,blank=True)
    Title = models.CharField(max_length=50,null=False,blank=False)
    Text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = create_slug(self.Title)
        super().save(*args, **kwargs)

    