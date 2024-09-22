from django.shortcuts import render

# 首頁視圖
def index(request):
    return render(request, 'index.html')

# 3D Viewer 視圖
def viewer(request):
    file = request.GET.get('file', '')
    param1 = request.GET.get('param1', '')
    param2 = request.GET.get('param2', '')

    # 這裡可以處理模型的展示邏輯，將參數傳遞到前端
    context = {
        'file': file,
        'param1': param1,
        'param2': param2,
    }
    
    return render(request, 'viewer.html', context)
