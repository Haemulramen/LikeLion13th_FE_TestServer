from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    @staticmethod
    def get_user_by_username(username):
        try:
            return User.objects.get(username=username)
        except Exception as e:
            return None