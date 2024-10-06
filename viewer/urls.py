from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # 其他 URL 路徑
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)