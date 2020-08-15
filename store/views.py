from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cartData, cookieCart, guestOrder



# Create your views here.

def home(request):
    products = Product.objects.all()

    data = cartData(request)
    cartItem = data['cartItem']
    context = {'products': products,'cartItem':cartItem}
    return render(request,'store/store.html',context)

def check(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItem = data['cartItem']
    context = {'items':items,'order':order,'cartItem':cartItem}
    return render(request,'store/checkout.html',context)

def chart(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItem = data['cartItem']
    context = {'items':items,'order':order,'cartItem':cartItem}
    return render(request,'store/chart.html',context)


def updateData(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print('productId: ',productId)
    # print('Actions:',action)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    
    return JsonResponse("data is added", safe=False)

# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
def orderProcess(request):
    # print('data',request.body)
    transition_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) 
    else:
        customer, order = guestOrder(request,data)
    ## ---------common part--------------
    total = data['form']['total']
    order.transaction_id = transition_id
    if str(total) == str(order.get_total_total):
        order.complete = True   
    order.save()
    if order.shipping == True:
        ShippingAdress.objects.create(
            customer= customer,
            order = order,
            addess = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
    return JsonResponse("Payment completed", safe=False)


## user info

def login(request):
    context ={}
    return render(request,'store/login.html',context)

def register(request):
    context={}
    return render(request,'store/register.html',context)