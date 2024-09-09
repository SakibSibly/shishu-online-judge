from django.db import models
from problems.models import Problem


class Contest(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContestProblem(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    all_problems = models.ManyToManyField(Problem)

    def __str__(self):
        return self.all_problems[0].title
