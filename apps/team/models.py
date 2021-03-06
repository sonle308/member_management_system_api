from django.db import models
from django.contrib.contenttypes.models import ContentType
from apps.user.models import CreatedUpdatedBase
from django.contrib.auth import get_user_model

User = get_user_model()

class Team(CreatedUpdatedBase):
    class Meta:
        db_table = 'team'

    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    description = models.TextField()
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="leader_user"
    )
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
