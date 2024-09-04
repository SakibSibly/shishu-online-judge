from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    t_shirt_size = models.CharField(max_length=10)
    university = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     db_table = 'users'
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
