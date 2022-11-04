from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.apps import apps
from home.models import Image
from home.utils.data import *
import json

@user_passes_test(lambda u: u.is_superuser)
def bg_home(request):
    return update_image(request, 'bg-home')

@user_passes_test(lambda u: u.is_superuser)
def profile_picture(request):
    return update_image(request, 'profile-picture')

@user_passes_test(lambda u: u.is_superuser)
def import_json(request):
    # check request method
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)
 
    # read data
    data = json.load(request.FILES['json-file'])

    # clear previous data
    for model in apps.get_app_config('home').get_models():
        if model != Image:
            model.objects.all().delete()

    # import data
    import_info(data['info'])
    import_services(data['services'])
    import_sections(data['sections'])
    import_social_medias(data['social_medias'])
    import_fields(data['fields'])
    import_projects(data['projects'])

    return JsonResponse({'status': 'success'})
