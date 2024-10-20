from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .form import UploadFileForm

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)  # 保存檔案
            uploaded_file_url = fs.url(filename)  # 獲取檔案的URL
            return render(request, 'viewer.html', {'file_url': uploaded_file_url})
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})

def viewer(request):
    file_url = request.GET.get('file_url', None)
    return render(request, 'viewer.html', {'file_url': file_url})
