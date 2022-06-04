from django.utils import timezone
from django.utils.text import slugify


def slugify_pre_save(sender,instance,*args, **kwargs):
    name = instance.name 
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(name)