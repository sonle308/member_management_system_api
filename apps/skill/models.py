from django.db import models
from django.contrib.contenttypes.models import ContentType

from apps.user.models import CreatedUpdatedBase, User
from django.contrib.auth import get_user_model

# User = get_user_model()

class Skill(CreatedUpdatedBase):
    class Meta:
        db_table = 'skill'

    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    used_year_number = models.IntegerField(default=0)
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="leader_skill",
    )

    def __str__(self):
        return self.name
