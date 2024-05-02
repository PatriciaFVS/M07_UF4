from django.db import models

class Usuari (models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100)
    cognom=models.CharField(max_length=100)
    assignatures=models.CharField(max_length=100)
    rol=models.CharField(max_length=100)
    
