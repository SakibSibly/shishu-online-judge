from django.db import models
from accounts.models import CustomUser


class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    input_type = models.CharField(max_length=10)
    output_type = models.CharField(max_length=10)
    tags = models.CharField(max_length=255, blank=True, null=True)
    difficulty = models.CharField(max_length=255)
    time_limit = models.IntegerField(default=1)
    memory_limit = models.IntegerField(default=255)
    note = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255,blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InputOutput(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.problem.title


class SolvedData(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    source_code = models.TextField()
    language = models.IntegerField()
    run_time = models.FloatField()
    solved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} : {self.problem.title}"
