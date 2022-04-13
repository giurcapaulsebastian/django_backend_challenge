from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('products')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('products')
            else:
                messages.info(request, 'Username OR password is incorrect!')

        context = {}
        return render(request, 'products/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

class ProductsView(ListView):
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

# @login_required(login_url='login_user')
# def products(request):
#     return render(request, 'products/products.html')

@login_required(login_url='login_user')
def nutrition(request):
    return render(request, 'products/nutrition.html')