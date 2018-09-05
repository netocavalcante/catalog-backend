# Create your views here.
from logging import exception

from django.core.exceptions import  ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
# from rest_framework import viewsets

from .models import *
from rest_framework import viewsets
from .serializers import SamuSerializer


import urllib.request, json

# class SamuView(viewsets.ModelViewSet):
#     queryset = Samu.objects.all()
#     serializer_class = SamuSerializer


S = []
def index(request):
    #el = modify()
    el = getDataFromJson()
    for io in el:
         print(io.objetivo)

    return HttpResponse(io.objetivo, content_type='application/json')

def getDataFromJson():
    data = urllib.request.urlopen(
        "http://servicos.al.gov.br/api/services.json?q=urgencia").read().decode(
        'utf8')
    element = json.loads(data)
    nome_property = element['services']
    for obj in nome_property:
        services = Servico()
        control = '';
        for el in obj['categories']:
            control = el['name']
            if el['name'] != 'Saúde':
                break

        if control != 'Saúde':
            continue

        services.categoria = obj['categories'][0]['name']
        services.idRef = obj['id']
        services.objetivo = obj["name"]
        services.tipo = 'urgencia'
        print(services)
        S.append(services)
        # services.
        services.save()
        for unit in obj["units"]:
            try:
                idRef = UnidadeSaude.objects.get(idRef=unit['id'])
                services.unit.add(idRef)

            except ObjectDoesNotExist as e:
                insertUnidadeSaude(unit)

        services.save()
        # insertUnidadeSaude(obj["units"])

        #buscar aqui os dados que estao no banco

    return S

def insertUnidadeSaude(unidade):

    # for unit in unidade :
       us = UnidadeSaude()
       us.idRef = unidade['id']
       us.descricao = unidade['name']
       us.address = unidade['address']
       us.municipio = unidade['county']
       try:
         us.save()
       except IntegrityError as e:
          print('ja cadastrado')


    # return unit


def createHospitais():
    data = urllib.request.urlopen(
        "http://dados.al.gov.br/dataset/a10e9c93-2fb8-4c38-84b4-43d69f0269f7/resource/bf7c7df7-c901-4218-bb22-da6aed11fc9f/download/unidadesdesaude.json").read().decode(
        'utf8')
    element = json.loads(data)

    nome_property = element['features']
    for obj in nome_property:
        hospital = Hospitais()
        hospital.nome =  obj['properties']['Nome']
        hospital.endereco = obj['properties']['Endereço']
        geometry_array = obj['geometry']['coordinates']

        try:

            hospital.x_coordinate = geometry_array.pop(0)

            hospital.y_coordinate = geometry_array.pop(0)

            print(hospital.nome)
            print(hospital.x_coordinate)
            print(hospital.y_coordinate)
            # samu.z_coordinate = geometry_array.pop(2)
            hospital.save(hospital)

        except Exception as error:
            print(error)
        # S.append(samu)
        # samu.save(S)

    return hospital


def modify():
    data = urllib.request.urlopen("http://dados.al.gov.br/dataset/fa88daf0-7510-49a3-8463-8d28a9d5dfc2/resource/65f98c86-1c25-446b-ac1d-05cee952617a/download/base.geojson").read().decode('utf8')
    element = json.loads(data)

    nome_property = element['features']
    for obj in nome_property:
        samu = Samu()
        c = obj['properties']['Nome']
        samu.nome = c
        geometry_array = obj['geometry']['coordinates']

        try:

         samu.x_coordinate = geometry_array.pop(0)

         samu.y_coordinate = geometry_array.pop(0)

         print(samu.nome)
         print(samu.x_coordinate)
         print(samu.y_coordinate)
         # samu.z_coordinate = geometry_array.pop(2)
         #samu.save(samu)

        except Exception as error:
            print(error)
        # S.append(samu)
        # samu.save(S)

    # print(S)
    # print(geometry_array.pop(2))
        # for coordinate in geometry_array:

    return samu
