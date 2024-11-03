from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),  # homepage
    path('Viewer/', views.viewer, name = 'Viewer'), # viewer page
    path('AR_Viewer/', views.AR_Viewer, name = 'AR_Viewer') # AR page
]
