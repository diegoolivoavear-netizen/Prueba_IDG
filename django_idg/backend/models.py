from django.db import models

class Usuario(models.Model):
    last_login = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=100)
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.username

