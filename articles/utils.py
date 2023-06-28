import random
from django.utils.text import slugify

def slugify_instance_title(instance, save=False, new_slug=None):
    # get slug from parameters or slugify current title
    if new_slug is not None:
        slug = new_slug
    else:  
        slug = slugify(instance.title)
    # filter by slug, exclude current instance
    Klass = instance.__class__ # make it run on any django model
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    # if slug exists in other instances
    if qs.exists():
        # create new slug using current one
        rand_int = random.randint(100_000, 900_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance