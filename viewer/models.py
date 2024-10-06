# models.py
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # 文件會被上傳到 media/uploads/ 文件夾
    uploaded_at = models.DateTimeField(auto_now_add=True)
