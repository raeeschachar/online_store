from django.contrib.auth.views import logout
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from user_sessions.forms import LoginForm, UserRegistrationForm


class HomePageView(View):
    template_name = 'online_store/home.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'user_sessions/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('online_store:home')


class AddUserView(View):
    template_name = 'user_sessions/registration.html'
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
