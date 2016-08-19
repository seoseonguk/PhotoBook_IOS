from django.conf import settings
from django.db import models

class User(models.Model):
    auth_user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.auth_user.username

    def as_dict(self):
        return {
            'id': self.id,
            'user': self.auth_user.username
        }

class Group(models.Model):
    owner = models.ForeignKey(User)
    user_list = models.ManyToManyField(User, related_name='user_list')
    name = models.CharField(max_length=15)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'owner' : self.owner.id,
            'user_list' : self.user_list.all().values('id'),
            'name' : self.name,
            'image_url' : self.image.url,
            'created_at' : self.created_at,
        }