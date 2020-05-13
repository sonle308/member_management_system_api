from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager


class CreatedUpdatedBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class User(AbstractBaseUser, CreatedUpdatedBase):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, unique=True)
    is_activate = models.BooleanField(default=False)
    avatar = models.ImageField(verbose_name='avatar', upload_to='images/')
    birthday = models.DateTimeField()
    is_superuser = models.BooleanField(default=False)
    skill = models.ManyToManyField('skill.Skill')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
