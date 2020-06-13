from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_customers': total_customers,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required(login_url='login')
def customer(request, customerId):
    customers = Customer.objects.get(id=customerId)
    orders = customers.order_set.all()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    orders_count = orders.count()

    context = {
        'customers': customers,
        'orders': orders,
        'orders_count': orders_count,
        'myFilter': myFilter
    }

    return render(request, 'customer.html', context)


@login_required(login_url='login')
def createOrder(request, customerId):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=customerId)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, orderId):
    order = Order.objects.get(id=orderId)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        # print('printing post', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, orderId):
    order = Order.objects.get(id=orderId)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'order': order}

    return render(request, 'delete.html', context)
