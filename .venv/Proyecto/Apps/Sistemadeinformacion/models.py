from operator import length_hint
from pyexpat import model
import uuid
from django.db import models
from geopy.geocoders import Nominatim
 

# Create your models here.
class rolLider(models.Model):
    cedula=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    ciudad=models.CharField(max_length=30)
    foto=models.ImageField(upload_to='albums/images/')

#Create model voting tables
# class mesasDevotacion(models.Model):
#     idPuesto=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)   
#     nombreMunicipio=models.CharField(max_length=25)
#     idMunicipio=models.IntegerField(max_length=20)
  
 #create model  votantes
class Votantes(models.Model):
         nombres=models.CharField(max_length=70)
         Apellidos=models.CharField(max_length=60)
         Telefono=models.IntegerField()
         Cedula=models.IntegerField()
         liderId=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
         barrioId=models.IntegerField()
         puestodevotacionId=models.IntegerField()
         mesa=models.CharField(max_length=50)