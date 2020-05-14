from django.contrib.auth.models import AbstractUser
from django.db import models


class CreatedUpdatedBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(verbose_name='avatar', upload_to='images/')
    birthday = models.DateTimeField()
    skill = models.ManyToManyField('skill.Skill')

    class Meta:
        db_table = 'user'
        ordering = ['-id']

    def __str__(self):
        return self.username
