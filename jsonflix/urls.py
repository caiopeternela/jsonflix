from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('v1/api/', views.api)
]
