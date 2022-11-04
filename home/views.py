from django.shortcuts import render
from django.db import models
from home.utils import serialized_objects, try_get_image
from home.models import *

def home(request):
    return render(request, 'home.html', {
        'data': {
          'info': {info.name: info.value for info in Info.objects.all()},
          'fields': serialized_objects(Field),
          'social_medias': serialized_objects(SocialMedia),
          'sections': serialized_objects(Section),
          'services': serialized_objects(Service),
          'projects': serialized_objects(Project),
          'bg_home_src': try_get_image('bg-home'),
          'profile_picture_src': try_get_image('profile-picture')
        }
   })
