from django.http import JsonResponse
from django.db import models
from home.models import Image


def update_image(request, name: str) -> JsonResponse:
    '''update an image based on name'''

    if request.method == 'POST':
        try:
            image = Image.objects.get(name=image)
        except:
            image = Image(name=name)
        
        image.image = request.FILES[name]
        image.save()

    return JsonResponse({'success': True})


def try_get_image(name) -> str|None:
    '''return src of image if exists'''

    try:
        return Image.objects.get(name=name).image.url
    except Image.DoesNotExist:
        return None
