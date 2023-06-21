from django.db import models
from Home.models import Service as Service
# Create your models here.
class Testimonial(models.Model):
    quote = models.TextField(max_length=1000)
    reviewer = models.CharField(max_length=55)
    rating = models.PositiveSmallIntegerField(choices=(
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    ))

class Project(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)
    service = models.ForeignKey('Home.Service', on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(upload_to='gallery/', null=True)

class ProjectGallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)
