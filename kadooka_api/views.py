from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'Hello, World!',
        'status': 'success',
        'version': '1.0.0'
    }, status=200)