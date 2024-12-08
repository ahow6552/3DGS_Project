from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import secure_serve
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 表單頁面
    path('upload', views.upload, name='upload'),  # 表單提交處理
    path('viewer', views.viewer, name='viewer'),  # 顯示 viewer 頁面
]

if settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>', secure_serve, {'document_root': settings.MEDIA_ROOT}),
        path('static/<path:path>', secure_serve, {'document_root': settings.STATICFILES_DIRS[0]}),
    ]
