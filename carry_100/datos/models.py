from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField( max_length=120 )
    descripcion = models.TextField()

    def __unicode__(self):
        return self.nombre

class Subcategoria(models.Model):
    foranea_tipo = models.ForeignKey( Tipo )
    nombre = models.CharField( max_length=120 )

    def __unicode__(self):
        return self.nombre

class Lenguaje(models.Model):
    foranea_tipo = models.ForeignKey( Tipo )
    foranea_subcat = models.ForeignKey( Subcategoria )

    nombre = models.CharField( max_length=120 )

    def __unicode__(self):
        return self.nombre