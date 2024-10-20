from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # homepage
    path('viewer/', views.viewer, name='viewer'), # viewerpage
]
