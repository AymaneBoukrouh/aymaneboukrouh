from django.db import models


def create_if_not_exists(model: models.Model, **kwargs) -> models.Model:
    '''create an instance of a model if it does not exist'''
    
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return model(**kwargs)


def serialized_objects(model: list[models.Model]) -> list[dict]:
    '''return serialized list of objects from a model'''

    return [obj.serialize() for obj in model.objects.all()]
