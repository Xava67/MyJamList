"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

def get_default_user():
    User = get_user_model()
    default_user, created = User.objects.get_or_create(username='HS', defaults={
        'email': 'haniasmolej@gmail.com',
    })
    return default_user.id

class Songs(models.Model):
    
    title = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(0, 6)])
    link = models.URLField()
    file = models.FileField(upload_to='songs/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    def __str__(self):
        return self.title
    
    def get_all_attributes(self):
        return {
            'title': self.title,
            'rating': self.rating,
            'link': self.link,
            'file': self.file.url,
        }




