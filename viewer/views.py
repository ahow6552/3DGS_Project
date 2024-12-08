from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def my_view(request):
    response = HttpResponse('Hello, world!')
    response['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response['Cross-Origin-Opener-Policy'] = 'same-origin'
    return response

def index(request):
    return render(request, 'index.html')

def viewer(request):
    file_url = 'media/point_cloud.ply'
    return render(request, 'viewer.html', {'file_url': file_url})

def AR_Viewer(request):
    file_url = request.GET.get('file_url', None)
    return render(request, 'AR_Viewer.html', {'file_url': file_url})