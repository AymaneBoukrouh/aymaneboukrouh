from django.db import models
from home.utils.object import create_if_not_exists
from home.models import *

def import_info(data: dict) -> None:
    '''import info from json data'''

    for name, value in data.items():
        info = create_if_not_exists(Info, name=name)
        info.value = value
        info.save()


def import_services(data: list[dict]) -> None:
    '''import services from json data'''

    for service in data:
        service_ = create_if_not_exists(Service, title=service['title'])
        service_.save()


def import_sections(data: list[dict]) -> None:
    '''import sections from json data'''

    for section in data:
        section_ = create_if_not_exists(Section, title=section['title'])
        section_.icon = section['icon']
        section_.save()


def import_social_medias(data: list[dict]) -> None:
    '''import social medias from json data'''

    for social_media in data:
        social_media_ = create_if_not_exists(SocialMedia, name=social_media['name'])
        social_media_.url = social_media['url']
        social_media_.icon = social_media['icon']
        social_media_.save()


def import_fields(data: list[dict]) -> None:
    '''import fields from json data'''
    
    for field in data:
        field_ = create_if_not_exists(Field, name=field['name'])
        field_.save()

        for technology in field['technologies']:
            technology_ = create_if_not_exists(Technology, name=technology)
            # TODO: implement technology_.field = field_
            technology_.save()

            field_technology = create_if_not_exists(FieldTechnology, technology=technology_, field=field_)
            field_technology.save()
        

def import_projects(data: list[dict]) -> None:
    '''import projects from json data'''

    for project in data:
        project_ = create_if_not_exists(Project, title=project['title'])
        project_.description = project['description']
        project_.save()

        for link in project['links']:
            link_ = create_if_not_exists(ProjectLink, icon=link['icon'], project=project_)
            link_.url = link['url']
            link_.icon = link['icon']
            link_.project = project_
            link_.save()

        for technology in project['technologies']:
            technology_ = create_if_not_exists(Technology, name=technology)
            technology_.save()
            
            project_technology = create_if_not_exists(ProjectTechnology, project=project_, technology=technology_)
            project_technology.save()
