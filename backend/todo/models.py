from django.db import models

def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.title), filname])



class Product(models.Model):
    title = models.CharField(max_length=32, blank=False)
    nameFile = models.ImageField(blank=True, null=True, upload_to=upload_path)

class Email(models.Model):
    email = models.CharField(max_length=100, blank=False,)
    