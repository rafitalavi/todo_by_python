from django.db import models
from django.contrib.auth.models import User  # 👈 Import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👈 Link to user
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    class Meta:
        ordering = ['created_at']    
