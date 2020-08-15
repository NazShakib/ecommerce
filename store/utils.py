import json
from . models import *

def cookieCart(request):
    items =[]
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart={}
    order = {'get_total_total':0,'get_total_item':0,'shipping': False}
    cartItem = order['get_total_item']
    for i in cart:
        try:
            cartItem += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price*cart[i]['quantity'])
            order['get_total_total'] += total
            order['get_total_item'] += cart[i]['quantity']
            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity': cart[i]['quantity'],
                'get_total':total
            }
            items.append(item)
            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'items':items,'order':order,'cartItem':cartItem}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        cookie = cookieCart(request)
        items = cookie['items']
        order = cookie['order']
        cartItem = cookie['cartItem']
    return {'items':items,'order':order,'cartItem':cartItem}

def guestOrder(request, data):
    print('You are not login....')
    print('COOKIE',request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']
    cookiesData = cookieCart(request)
    items = cookiesData['items']
    customer, created = Customer.objects.get_or_create(
        email= email,
    )
    customer.name = name
    customer.save()
    order = Order.objects.create(
        customer = customer,
        complete = False
    )
    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product = product,
            order = order,
            quantity = item['quantity']  
        )
    return customer, order