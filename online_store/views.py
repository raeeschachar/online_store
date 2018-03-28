from django.shortcuts import render
from django.views import View


class HomePageView(View):
    template_name = 'online_store/home.html'

    def get(self, request):
        return render(request, self.template_name)
