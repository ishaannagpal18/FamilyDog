from django.db import models

# Create your models here.


class Adoptions(models.Model):
    mainimage1 = models.ImageField(upload_to='Adoption')
    mainimage2 = models.ImageField(upload_to='Adoption')
    mainimage3 = models.ImageField(upload_to='Adoption')
    mainimage4 = models.ImageField(upload_to='Adoption')
    mainimage5 = models.ImageField(upload_to='Adoption')
    mainimage6 = models.ImageField(upload_to='Adoption')
    mainimage7 = models.ImageField(upload_to='Adoption')
    mainimage8 = models.ImageField(upload_to='Adoption')
    mainimage9 = models.ImageField(upload_to='Adoption')
    mainimage10 = models.ImageField(upload_to='Adoption')
    mainimage11 = models.ImageField(upload_to='Adoption')
    mainimage12 = models.ImageField(upload_to='Adoption')
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name
