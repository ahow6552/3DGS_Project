from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.static import serve

# 表單頁面
def index(request):
    return render(request, 'index.html')

def secure_serve(request, path, document_root=None, show_indexes=False):
    response = serve(request, path, document_root=document_root, show_indexes=show_indexes)
    response['Cross-Origin-Opener-Policy'] = 'same-origin'
    response['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

# 接收表單提交並處理相機選擇
def upload(request):
    if request.method == 'POST':
        # 提取 cameraId
        camera_id = request.POST.get('cameraId')
        if not camera_id:
            return JsonResponse({'status': 'error', 'message': 'No camera selected'}, status=400)

        # 可根據需求進行其他處理（例如存儲到 session 或數據庫）

        # 將 cameraId 傳遞到 viewer 頁面
        return redirect(f'/viewer?cameraId={camera_id}')
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

# 顯示 viewer 頁面
def viewer(request):
    return render(request, 'viewer.html')
