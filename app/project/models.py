from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from app.user.models import CreatedUpdatedBase
from app.team.models import Team


class Project(CreatedUpdatedBase):
    class Meta:
        db_table = 'project'

    project_leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="leader_project",
    )
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    team = models.ManyToManyField(Team)
    user = models.ManyToManyField(User)
