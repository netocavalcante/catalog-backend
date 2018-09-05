from django.urls import path,include
from . import views
from rest_framework import routers
from .viewsets import SamuView
from .viewsets import HospitalView


router = routers.DefaultRouter()
router.register(r'saude', SamuView)
router.register(r'hospitais', HospitalView)

urlpatterns = [
    path('' , include(router.urls)),
    path('teste/', views.index, name='index')
]