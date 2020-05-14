from django.db import models

from apps.user.models import CreatedUpdatedBase


class Skill(CreatedUpdatedBase):
    class Meta:
        db_table = 'skill'

    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    used_year_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name
