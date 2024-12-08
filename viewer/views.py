from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def viewer(request):
    file_url = 'media/point_cloud.ply'
    return render(request, 'viewer.html', {'file_url': file_url})

def AR_Viewer(request):
    file_url = request.GET.get('file_url', None)
    return render(request, 'AR_Viewer.html', {'file_url': file_url})