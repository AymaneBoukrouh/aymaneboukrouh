from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from home.models import Image

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def profile_picture(request):
    if request.method == 'POST':
        try:
            image = Image.objects.get(name='profile-picture')
        except Image.DoesNotExist:
            image = Image(name='profile-picture')
        
        image.image = request.FILES['profile-picture']
        image.save()

    return JsonResponse({
        'status': 'success'
    })
