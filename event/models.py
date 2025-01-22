from django.db import models
from uuslug import uuslug
# Create your models here.

class odel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Location(odel):
    location=models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural='Locations'

    def __str__(self):
        return self.location


class Event(odel):
    slug = models.SlugField(max_length=255, null=True, blank=True)
    title=models.CharField(max_length=150, null=True)
    description=models.TextField(null=True, blank=True)
    file=models.FileField(upload_to='events/', null=True)
    time=models.DateTimeField(null=True)
    duration=models.DurationField(null=True)
    location=models.ForeignKey(Location, on_delete=models.CASCADE,related_name='blogs')
    speaker=models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
         return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = uuslug(self.title, instance=self)
        super(Event,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
