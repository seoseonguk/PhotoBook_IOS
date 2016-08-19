from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


from users.models import User, Group



def image_upload_to(instance, filename):
    title = instance.moment.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
    return "photos/%s/%s" %(slug, new_filename)


class Photo(models.Model):
    liked = models.BooleanField(default=0)
    owner = models.ForeignKey(User)
    image = models.ImageField(upload_to=image_upload_to)
    moment = models.ForeignKey('Moment')
    taken_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.moment, self.id)

    def get_absolute_url(self):
        return reverse('photo:photo_detail', kwargs={'pk':self.pk})


class Moment(models.Model):
    group = models.ForeignKey(Group)
    title = models.CharField(max_length=120, blank=True, null=True)
    # image = models.ImageField(blank=True)
    taken_at = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.taken_at)