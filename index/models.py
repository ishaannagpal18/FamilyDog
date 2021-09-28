from django.db import models

# Create your models here.
class about(models.Model):

    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=800, blank=False)


    def __str__(self):
        return self.title

class slider(models.Model):

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    image=models.ImageField(upload_to='slider/')
    def __str__(self):
        return self.title

class featuredservices(models.Model):
    bibiclass=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    def __str__(self):
        return self.title

class services(models.Model):
    bibiclass=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    def __str__(self):
        return self.title

class clients(models.Model):
    image=models.ImageField(upload_to='clients/')


class portfolio(models.Model):
    image=models.ImageField(upload_to='portfolio/', blank=False)

class testimonial(models.Model):
    name=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    quote=models.CharField(max_length=800)
    def __str__(self):
        return self.name

class contactlist(models.Model):
    address = models.TextField(max_length=800, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.email

class contactform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=800, blank=False)
    def __str__(self):
        return self.name
