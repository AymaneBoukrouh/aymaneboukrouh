from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from home.models import *
import json

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

@user_passes_test(lambda u: u.is_superuser)
def import_json(request):
    # TODO: clear all data before importing

    if request.method == 'POST':
        json_file = request.FILES['json-file']
        data = json.load(json_file)

        for key, value in data['info'].items():
            try:
                info = Info.objects.get(name=key)
            except Info.DoesNotExist:
                info = Info(name=key)
            
            info.value = value
            info.save()

        for service in data['services']:
            try:
                service_ = Service.objects.get(title=service['title'])
            except Service.DoesNotExist:
                service_ = Service(title=service['title'])

            service_.save()

        for section in data['sections']:
            try:
                section_ = Section.objects.get(title=section['title'])
            except Section.DoesNotExist:
                section_ = Section(title=section['title'])

            section_.icon = section['icon']
            section_.save()   

        for social_media in data['social_medias']:
            try:
                social_media_ = SocialMedia.objects.get(name=social_media['name'])
            except SocialMedia.DoesNotExist:
                social_media_ = SocialMedia(name=social_media['name'])

            social_media_.url = social_media['url']
            social_media_.icon = social_media['icon']
            social_media_.save() 

        for technology in data['technologies']:
            try:
                technology_ = TechnologyField.objects.get(name=technology['name'])
            except TechnologyField.DoesNotExist:
                technology_ = TechnologyField(name=technology['name'])

            technology_.save()
            
            for element in technology['elements']:
                try:
                    element_ = Technology.objects.get(name=element)
                except Technology.DoesNotExist:
                    element_ = Technology(name=element)

                element_.save()
            
                try:
                    field_technology = FieldTechnology.objects.get(technology=element_, field=technology_)
                except FieldTechnology.DoesNotExist:
                    field_technology = FieldTechnology(technology=element_, field=technology_)
                    field_technology.save()


        for project in data['projects']:
            try:
                project_ = Project.objects.get(title=project['title'])
            except Project.DoesNotExist:
                project_ = Project(title=project['title'])

            project_.description = project['description']
            project_.save()

            for link in project['links']:
                try:
                    link_ = ProjectLink.objects.get(icon=link['icon'], project=project_)
                except ProjectLink.DoesNotExist:
                    link_ = ProjectLink(icon=link['icon'], project=project_)
                
                link_.url = link['url']
                link_.icon = link['icon']
                link_.project = project_
                link_.save()

            for technology in project['technologies']:
                try:
                    technology_ = Technology.objects.get(name=technology)
                except Technology.DoesNotExist:
                    technology_ = Technology(name=technology)
                
                technology_.save()

                try:
                    project_technology = ProjectTechnology.objects.get(project=project_, technology=technology_)
                except ProjectTechnology.DoesNotExist:
                    project_technology = ProjectTechnology(project=project_, technology=technology_)
                    project_technology.save()

        return JsonResponse({
            'status': 'success'
        })
