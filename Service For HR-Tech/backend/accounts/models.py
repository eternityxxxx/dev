from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# class User(AbstractBaseUser):
#     first_name = models.CharField(max_length=128, verbose_name='Firstname')
#     last_name = models.CharField(max_length=128, verbose_name='Lastname')
#     email = models.EmailField(db_index=True, unique=True, verbose_name='Email')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Account creation time')
#     updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Account update time')
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     def get_full_name(self):
#         return str(self.first_name) + ' ' + str(self.last_name)
#
#     def get_short_name(self):
#         return str(self.first_name)
#
#     def __str__(self):
#         return self.email
#
#
# class Admin(User):
