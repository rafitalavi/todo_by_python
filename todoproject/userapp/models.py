from django.contrib.auth.models import User
from django.db import models
from roleapp.models import Role


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # Removed email field to avoid duplication

    def __str__(self):
        return f"{self.user.username} ({self.user.email})"
