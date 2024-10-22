from django.db import models

# Create your models here.
class Generos(models.Model):
    generos_id=models.AutoField(primary_key=True)
    nombre_generos= models.CharField(max_length=255)
    
    class Meta:
        db_table = "generos"



class Usuarios(models.Model):
    usuario_id =    models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(Generos, on_delete=models.CASCADE,default=0)
    class Meta:
        db_table = "usuarios"