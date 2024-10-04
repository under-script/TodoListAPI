from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Todo(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'], name='unique_todo_per_user')
        ]

    def __str__(self):
        return self.title