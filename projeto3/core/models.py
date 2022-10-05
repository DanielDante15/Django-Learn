from enum import unique
from re import T
from django.db.models import *
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = EmailField(unique=True)
