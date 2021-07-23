from django.db import models

# Create your models here.

class Clientes(models.Model):
    rut = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

class Empresas(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Arriendos(models.Model):
    costo_diario = models.IntegerField()
    dias = models.IntegerField()
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)