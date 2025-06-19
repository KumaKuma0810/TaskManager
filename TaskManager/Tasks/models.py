from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    descrioption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
