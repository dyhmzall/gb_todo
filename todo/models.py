from django.db import models
from user.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=128, blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.text if len(str(self.text)) <= 16 else self.text[0:16] + '...'
