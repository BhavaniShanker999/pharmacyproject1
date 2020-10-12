from django.shortcuts import render,redirect
from django.http import HttpResponse


# for the mutiple forms adn messages
from django.forms import inlineformset_factory

#all the imports related to models,filters,forms
from .models import *
from .forms import *
from .filters  import *

# registration and login related imports and messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def registration_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	form=create_user_form()
	if request.method=='POST':
		form =create_user_form(request.POST)
		if form.is_valid():
			form.save()
			user_name=form.cleaned_data.get('username')
			messages.success(request,'Account was created for'+ user_name)
			return redirect('login_page')

	context={'form':form}
	return render(request,'accounts/registration.html',context)

def login_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method=='POST':
		customer_username=request.POST.get('username')
		customer_password=request.POST.get('password')
		user= authenticate (request, username=customer_username, password=customer_password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username or Password Incorrect')
	context={}
	return render(request,'accounts/login.html',context)

def logout_user(request):
	logout(request)
	return redirect('login_page')





@login_required(login_url='login_page')
def home(request):
	customers=Customer.objects.all()
	customer_fil=customer_filter(request.GET,queryset=customers)
	customers=customer_fil.qs
	orders=Order.objects.all().order_by('-date_created')
	# orders count
	out_for_delivery = Order.objects.filter(
	status='Out For Delivery').count()
	delivered = Order.objects.filter(status='Delivered').count()
	total_orders = out_for_delivery+delivered
	context = {'customers': customers,'orders': orders,
	           'total_orders': total_orders,'out_for_delivery':out_for_delivery,
			   'delivered':delivered,'customer_fil':customer_fil}
	return render(request, 'accounts/dashboard.html',context)



def products(request):
	prod = Product.objects.all().order_by('-date_created')
	context={'prod':prod}
	return render(request,'accounts/products.html',context)


@login_required(login_url='login_page')
def customer(request,pk):
	customer=Customer.objects.get(id=pk)
	orders=customer.order_set.all()
	order_filter=customer_order_filter(request.GET, queryset=orders)
	orders_count=orders.count()
	orders=order_filter.qs
	context = {'customer': customer, 'orders': orders,'orders_count':orders_count,'order_filter':order_filter}
	return render(request, 'accounts/customer.html',context)


@login_required(login_url='login_page')
def create_order_customer(request,pk):
	order_formset=inlineformset_factory(Customer,Order,fields=('product','quantity','status'),extra=9)
	customer=Customer.objects.get(id=pk)
	form_set=order_formset(queryset=Order.objects.none(),instance=customer)
	if request.method=='POST':
		form_set = order_formset(request.POST,instance=customer)
		if form_set.is_valid():
			form_set.save()
			return redirect('home')
	context={'form_set':form_set,'customer':customer}
	return render(request,'accounts/create_order.html',context)


@login_required(login_url='login_page')
def update_order_customer(request,pk):
	order=Order.objects.get(id=pk)  
	form=create_order(instance=order)
	if request.method=='POST':
		form = create_order(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('home')
	context={'form':form}
	return render(request,'accounts/update_order.html',context)


@login_required(login_url='login_page')
def delete_order_customer(request,pk):
	ordered_item=Order.objects.get(id=pk)
	context={'ordered_item':ordered_item}
	if request.method=="POST":
		ordered_item.delete()
		return redirect('home')
	return render(request,'accounts/delete_order.html',context)


@login_required(login_url='login_page')
def create_customer(request):
	form=create_customer_form()
	if request.method=="POST":
		form=create_customer_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context={'form':form}
	return render(request,'accounts/create_customer.html',context)


@login_required(login_url='login_page')
def create_product(request):
	form=create_product_form()
	if request.method=="POST":
		form=create_product_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('products')
	context={'form':form}
	return render(request,'accounts/create_product.html',context)

@login_required(login_url='login_page')
def info(request):
	return render(request,'accounts/info.html')

