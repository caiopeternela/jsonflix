from django.urls import path
from django.views.generic.base import RedirectView, TemplateView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='docs')),
    path('api/v1/', views.api, name='api'),
    path('api/v1/all', views.all, name='all'),
    path('api/v1/docs', TemplateView.as_view(template_name='jsonflix/docs.html'), name='docs'),
]
