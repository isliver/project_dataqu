from rest_framework import serializers
from data_test import models

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = '__all__'

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresas
        fields = '__all__'

class ArriendosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Arriendos
        fields = '__all__'
