from django.db import models
from problems.models import Problem, SolvedData
from accounts.models import CustomUser


class Contest(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    registered_users = models.IntegerField(default=0)
    end_time = models.DateTimeField()
    duration = models.DurationField()
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContestProblem(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    all_problems = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return self.all_problems.title


class ContestRegData(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ContestSubmission(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    submission_details = models.ForeignKey(SolvedData, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    verdict = models.CharField(max_length=50)

    def __str__(self):
        return self.user + " | " + self.verdict


class ContestLeaderboard(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user + " | " + str(self.score)
