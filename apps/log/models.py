from django.db import models
from django.contrib.contenttypes.models import ContentType
from apps.user.models import CreatedUpdatedBase
from django.contrib.auth import get_user_model

User = get_user_model()

class Activity_Log(CreatedUpdatedBase):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_log"
    )
    time = models.DateTimeField()
    action = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        db_table = 'activity_log'
