from django.contrib.auth.hashers import make_password
from django.db import models

class User(models.Model):
    fullName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    userType = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email