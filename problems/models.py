from django.db import models


class Problems(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    input_description = models.TextField()
    output_description = models.TextField()
    tags = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    time_limit = models.CharField(max_length=255)
    memory_limit = models.CharField(max_length=255)
    note = models.TextField()
    source = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InputOutput(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()

    def __str__(self):
        return self.problem.title
