from django.contrib.auth.views import logout
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from user_sessions.forms import LoginForm


class LoginView(View):
    template_name = 'user_sessions/login.html'
    form = LoginForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('online_store:home')
