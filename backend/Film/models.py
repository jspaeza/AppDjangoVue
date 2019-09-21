from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=50)
    sinopsis = models.TextField()
    imagen = models.FileField(blank=False, null=True)
    
    def __str__(self):
        return self.imagen.name
  



