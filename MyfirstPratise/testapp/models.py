from django.db import models
from django.contrib.auth.models import User
#
# # Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=70)
#     last_name = models.CharField(max_length=70)
#     email = models.EmailField(max_length=100)
#     username = models.CharField(max_length=70)
#     password1 = models.CharField(max_length=70)
#     password2 = models.CharField(max_length=70)
#
#     def __str__(self):
#         return self.username


class Crudproject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    marks = models.IntegerField()


