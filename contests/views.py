from django.shortcuts import render
from django.views import View
from .models import Contest, ContestProblem


class ContestsView(View):
    def get(self, request):
        all_contests = Contest.objects.all()
        return render(request, 'contests/contests.html', {'all_contests': all_contests})
    
    def post(self, request):
        pass


class FetchContestView(View):
    def get(self, request, contest_id):
        fetched_contest = ContestProblem.objects.filter(contest=Contest.objects.filter(id=contest_id).first())
        return render(request, 'contests/individual_contest.html', {'fetched_contest': fetched_contest})
    
    def post(self, request, contest_id):
        pass