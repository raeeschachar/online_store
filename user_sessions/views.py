from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect

from user_sessions.forms import LoginForm


class LoginView(View):
    template_name = 'user_sessions/login.html'
    form = LoginForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=un, password=pw)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard:dashboard'))
            else:
                return render(request, self.template_name, {
                    'form': self.form(), 'error_message': 'Invalid Credentials'})
        else:
            return render(request, self.template_name, {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('online_store:home')
