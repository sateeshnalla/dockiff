from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.messages import get_messages

from .models import Product


# Create your views here.
class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('register:productslist')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('register:login')


class Register(TemplateView):
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        user_data = request.POST

        user_name = user_data.get('username')
        email = user_data.get('email')
        name = user_data.get('name')
        password = user_data.get('password')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email Taken")
            return redirect("register:register")

        if User.objects.filter(username=user_name).exists():
            messages.info(request, "User Name Taken")
            return redirect("register:register")

        user = User.objects.create_user(username=user_name,
                                        email=email,
                                        first_name=name,
                                        password=password)

        user.save()
        return redirect('home')


class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = authenticate(username=data.get('username'),
                            password=data.get('password'))
        if user is not None:
            login(request, user)
            return redirect('register:productslist')
        return redirect('register:login')


class ProdutsListView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            products = Product().get_user_products(request.user)
            return render(request,
                          template_name='products_list.html',
                          context={'products': products})
        return redirect('register:login')


class ProductCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request,
                          template_name='product_create.html',
                          context={'user': request.user})
        return redirect('register:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = request.POST
            name = data.get('name')
            price = int(data.get('price'))
            s_dec = data.get('short_description')
            l_dec = data.get('long_description')
            product = Product()
            product.create_product(user=request.user,
                                   name=name,
                                   s_dec=s_dec,
                                   price=price,
                                   l_dec=l_dec)
            return redirect('register:productslist')
        return redirect('register:login')