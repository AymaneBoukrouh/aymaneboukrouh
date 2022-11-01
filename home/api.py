from django.http import JsonResponse
from home.models import Image

def bg_home(request):
    if request.method == 'POST':
        try:
            image = Image.objects.get(name='bg-home')
        except Image.DoesNotExist:
            image = Image(name='bg-home')
        
        image.image = request.FILES['bg-home']
        image.save()

    return JsonResponse({
        'status': 'success'
    })