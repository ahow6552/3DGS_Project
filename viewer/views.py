# views.py
from django.shortcuts import render, redirect
from .forms import FileUploadForm

def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # 保存上傳的文件
            return redirect('success')  # 成功上傳後跳轉到成功頁面
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

# views.py
def success_view(request):
    return render(request, 'success.html')

