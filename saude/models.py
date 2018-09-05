from django.db import models


# Create your models here.

class Samu(models.Model):
    nome = models.CharField(max_length=200)
    geomtry_type = models.CharField(max_length=100)
    x_coordinate = models.DecimalField(max_digits=50,decimal_places=40)
    y_coordinate = models.DecimalField(max_digits=50,decimal_places=40)

class Hospitais(models.Model):
    nome = models.CharField(max_length=300)
    endereco = models.CharField(max_length=400)
    x_coordinate = models.DecimalField(max_digits=50, decimal_places=40)
    y_coordinate = models.DecimalField(max_digits=50, decimal_places=40)


class UnidadeSaude(models.Model):
    idRef = models.CharField(max_length=100, unique=True    ) # id ja existente e utilizado pelos dados aberto deve ser criado um novo
    descricao = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    municipio = models.CharField(max_length=100,null=True)
    coordinateX =  models.DecimalField(max_digits=10, decimal_places=10, null=True)
    coordinateY = models.DecimalField(max_digits=10, decimal_places=10, null=True)

class Servico(models.Model):
    idRef =  models.CharField(max_length=100) # id já utilizado pelo json, deve ser criado um id próprio
    categoria = models.CharField(max_length=50) # saude ou outra categoria
    descricao = models.CharField(max_length=500)
    objetivo = models.CharField(max_length=500) # campo name do json
    tipo = models.CharField(max_length=100) #campo que vai dizer se é urgencia ou emergencia
    unit = models.ManyToManyField(UnidadeSaude)
    coordinateX = models.DecimalField(max_digits=10, decimal_places=10,null=True)
    coordinateY = models.DecimalField(max_digits=10, decimal_places=10,null=True)
