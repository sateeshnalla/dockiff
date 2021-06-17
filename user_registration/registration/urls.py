from django.urls import path, include
from .views import  Register, Login, ProdutsListView, ProductCreateView

app_name = 'registration'

urlpatterns = [

    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('products/', ProdutsListView.as_view(), name='productslist'),
    path('productcreate/', ProductCreateView.as_view(), name='productcreate')
 ]