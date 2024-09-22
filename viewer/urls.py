from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 這是首頁
    path('viewer/', views.viewer, name='viewer'),  # 這是Viewer頁面
]
