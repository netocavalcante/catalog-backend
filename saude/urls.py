from django.urls import path,include
from . import views
from rest_framework import routers
from .viewsets import SamuView
from .viewsets import HospitalView
from .viewsets import UnidadeSaudeView
from .viewsets import ServicoVeiw

router = routers.DefaultRouter()
router.register(r'saude', SamuView)
router.register(r'hospitais', HospitalView)
router.register(r'unidadesaude', UnidadeSaudeView)
router.register(r'servico', ServicoVeiw)

urlpatterns = [
    path('' , include(router.urls)),
    path('teste/', views.index, name='index')
]