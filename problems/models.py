from django.db import models


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

    def __str__(self):
        return self.problem.title
