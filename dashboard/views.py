from django.shortcuts import render
from django.views import View

from products.models import Category, Product


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        product_list = Product.objects.all()
        return render(request, self.template_name, {'product_list': product_list})
