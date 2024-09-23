from django.contrib import admin
from .models import Contest, ContestProblem, ContestRegData, ContestSubmission, ContestLeaderboard


admin.site.register(Contest)
admin.site.register(ContestProblem)
admin.site.register(ContestRegData)
admin.site.register(ContestSubmission)
admin.site.register(ContestLeaderboard)
