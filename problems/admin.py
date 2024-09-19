from django.contrib import admin
from .models import Problem, InputOutput, SolvedData


admin.site.register(Problem)
admin.site.register(InputOutput)
admin.site.register(SolvedData)