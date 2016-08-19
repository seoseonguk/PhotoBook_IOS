from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


from users.models import User, Group



def image_upload_to(instance, filename):
    title = instance.memory.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
    return "photos/%s/%s" %(slug, new_filename)


class Photo(models.Model):
    owner = models.ForeignKey(User)
    image = models.ImageField(upload_to=image_upload_to)
    memory = models.ForeignKey('Memory')
    taken_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.memory, self.id)

    def get_absolute_url(self):
        return reverse('photo:photo_detail', kwargs={'pk':self.pk})


class Memory(models.Model):
    group = models.ForeignKey(Group)
    title = models.CharField(max_length=120, blank=True, null=True)
    # image = models.ImageField(blank=True)
    taken_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title