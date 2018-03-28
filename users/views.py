from django.shortcuts import render
from django.views import View
from users.forms import UserRegistrationForm


class AddUserView(View):
    template_name = 'users/registration.html'
    form = UserRegistrationForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()})
