from django import template

register = template.Library()

from ..models import Service, ServiceImage

def thumbnail(id):
    service = Service.objects.filter(pk=id).get()
    images = ServiceImage.objects.filter(service_id=id).all()
    for image in images:
        # is this image set to default or not?
        if image.is_default == True:
            # return url of current image and break out of loop.
            return image
            break

register.filter('thumbnail', thumbnail)

def stars(val):
    if val == 1:
       return "★☆☆☆☆"

    if val == 2:
        return "★★☆☆☆"

    if val == 3:
        return "★★★☆☆"

    if val == 4:
        return "★★★★☆"

    if val == 5:
        return "★★★★★"

register.filter('stars', stars)
