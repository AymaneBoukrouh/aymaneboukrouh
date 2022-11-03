from django.shortcuts import render
from home.models import *

def home(request):
    try:
        profile_picture_src = Image.objects.get(name='profile-picture').image.url
    except Image.DoesNotExist:
        profile_picture_src = None

    try:
        bg_home_src = Image.objects.get(name='bg-home').image.url
    except Image.DoesNotExist:
        bg_home_src = None

    return render(request, 'home.html', {
        'data': {
          'info': {info.name: info.value for info in Info.objects.all()},
          'technologies': [tf.serialize() for tf in TechnologyField.objects.all()],
          'social_medias': [social_media.serialize() for social_media in SocialMedia.objects.all()],
          'sections': [section.serialize() for section in Section.objects.all()],
          'services': [service.serialize() for service in Service.objects.all()],
          'projects': [project.serialize() for project in Project.objects.all()],
          'bg_home_src': bg_home_src,
          'profile_picture_src': profile_picture_src
        }
   })
