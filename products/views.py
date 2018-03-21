from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from models import Category, Product


def index(request):
    return HttpResponse("Test view of Online Store Main")


class ProductDetailView(View):
    template_name = 'products/product_detail.html'

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, self.template_name, {'product': product})
