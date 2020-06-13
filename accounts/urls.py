from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:customerId>', views.customer, name='customer'),
    path('create_order/<str:customerId>',
         views.createOrder, name='create_order'),
    path('update_order/<str:orderId>', views.updateOrder, name='update_order'),
    path('delete_order/<str:orderId>', views.deleteOrder, name='delete_order')
]
