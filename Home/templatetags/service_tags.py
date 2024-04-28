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


# write a template tag that will avoid overflowing service card (description) flip animation.
def service_description(description):

    # get the length of the description
    desc_len = len(description)

    # does the length of the description exceed 512 characters?
    if desc_len > 512:
        # need to re-process the string so that we don't overflow and return an ellipsis.

        # so we get the first 512 characters of the string. and join with an ellipsis.
        truncated_desc = description[0:512] + "..."

        # return this new truncated description
        description = truncated_desc

    return description


register.filter('service_description', service_description)
