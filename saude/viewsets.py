from .models import *
from rest_framework import viewsets
from .serializers import SamuSerializer
from .serializers import HospitaisSerializer
from .serializers import ServicoSerializer
from  .serializers import UnidadeSaudeSerializer

import urllib.request, json


class SamuView(viewsets.ModelViewSet):
    queryset = Samu.objects.all()
    serializer_class = SamuSerializer

class HospitalView(viewsets.ModelViewSet):
    queryset = Hospitais.objects.all()
    serializer_class = HospitaisSerializer

class ServicoVeiw(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class UnidadeSaudeView(viewsets.ModelViewSet):
    queryset = UnidadeSaude.objects.all()
    serializer_class = UnidadeSaude