from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from users.forms import UserRegistrationForm
from django.http import HttpResponseRedirect


class AddUserView(View):
    template_name = 'users/registration.html'
    form = UserRegistrationForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password1']
            user = authenticate(username=un, password=pw)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard:dashboard'))
        else:
            return render(request, self.template_name, {'form': form})
