from django.shortcuts import render, redirect
from . models import *
from .forms import OrderForm,CreateUserForm,CustomerForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticaed_user, allowed_users,admin_only
from django.contrib.auth.models import Group

# Create your views here.



@unauthenticaed_user
def usersignup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user)
            messages.success(request,'Account was Created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'signup.html',context)




@unauthenticaed_user
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('index')

        else:
            messages.info(request,'username or password incorrect.')
    context={}
    return render(request, 'login.html',context)



def userlogout(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def Profile(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    content = {'form':form}

    return render(request,'profile.html',content)






@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context={'orders':orders,'total_orders':total_orders,
    'delivered':delivered,'pending':pending}
    return render(request,'userpage.html',context)




@login_required(login_url='login')
@admin_only
def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()


    context = {'orders':orders,'customers':customers,'total_orders':total_orders,
    'total_customers':total_customers,'delivered':delivered,'pending':pending}
    return render(request, 'index.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products =  Product.objects.all()

    context = {'products':products}
    return render(request, 'products.html',context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    context = {'customer':customer,'orders':orders,'order_count':order_count,'myFilter':myFilter}
    return render(request, 'customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'order_form.html',context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)



    if request.method  == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'order_form.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context={'item':order}
    return render(request,'delete.html',context)
