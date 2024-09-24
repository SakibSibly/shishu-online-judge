from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.utils.http import urlencode
from django.db.models import Q
from .models import Contest, ContestProblem, ContestRegData


class ContestsView(View):
    def get(self, request):
        all_contests = Contest.objects.all()
        return render(request, 'contests/contests.html', {'all_contests': all_contests})
    
    def post(self, request):
        pass


class FetchContestView(View):
    def get(self, request, contest_id):
        if not request.user.is_authenticated:
            login_url = reverse('login') + '?' + urlencode({'next': request.path})
            return redirect(login_url)
        
        find_user = ContestRegData.objects.filter(Q(contest=Contest.objects.filter(id=contest_id).first()) & Q(user=request.user))
        if not find_user:
            user_redirect = reverse_lazy('register_contest', kwargs={'contest_id': contest_id})
            return redirect(user_redirect)

        fetched_contest = ContestProblem.objects.filter(contest=Contest.objects.filter(id=contest_id).first())
        return render(request, 'contests/individual_contest.html', {'fetched_contest': fetched_contest})
    
    def post(self, request, contest_id):
        pass


class RegisterContestView(View):
    def get(self, request, contest_id):
        if request.user.is_authenticated:
            find_user = ContestRegData.objects.filter(Q(contest=Contest.objects.filter(id=contest_id).first()) & Q(user=request.user))

            is_registered = False
            message = None

            if find_user:
                is_registered = True
                message = 'You are already registered for this contest'
            
            getContestData = Contest.objects.filter(id=contest_id).first()
            context = {
                'is_registered': is_registered,
                'contest': getContestData,
                'message': message
            }
            
            return render(request, 'contests/abstruction_page.html', context)
        login_url = reverse('login') + '?' + urlencode({'next': request.path})
        return redirect(login_url)
    
    def post(self, request, contest_id):
        getUser = ContestRegData.objects.filter(Q(contest=Contest.objects.filter(id=contest_id).first()) & Q(user=request.user))
        if not getUser:
            contestReg = ContestRegData(contest=Contest.objects.filter(id=contest_id).first(), user=request.user)
            contestReg.save()

        user_redirect = reverse_lazy('fetch_contest', kwargs={'contest_id': contest_id})
        return redirect(user_redirect)