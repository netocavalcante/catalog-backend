from rest_framework import serializers
from .models import Samu
from .models import Hospitais
from .models import UnidadeSaude
from .models import Servico

class SamuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samu
        fields = ('id','nome','x_coordinate','y_coordinate')

class HospitaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitais
        fields = ('id','nome','endereco','x_coordinate','y_coordinate')


class UnidadeSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeSaude
        fields = ('id','idRef', 'descricao' , 'address' , 'municipio' , 'coordinateX', 'coordinateY' )

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ('id' , 'idRef' , 'categoria' , 'descricao' , 'objetivo' , 'tipo' , 'coordinateX' , 'coordinateY')