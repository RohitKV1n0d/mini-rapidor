from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Order, OrderLines
from customer.models import customer as Customer
from products.models import product as Product
from django.views.decorators.csrf import csrf_exempt
import json






# Create your views here.

def index(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    product = Product.objects.all()
    return render(request, 'order/index.html', {'orders': orders, 'customers': customer, 'products': list(product.values()) })

def list_customers(request):
    customers = Customer.objects.all()
    return JsonResponse(list(customers.values()), safe=False)


@csrf_exempt
def add_order(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data)
        customer_c = data['customer_code']
        discount = data['discount']
        customer = Customer.objects.get(customer_code=customer_c)
        customer_name = customer.name
        order_date = datetime.now()
        total_without_discount = 0
        gross = 0
        order = Order.objects.create(customer_code=customer , customer_name=customer_name, order_date=order_date, total_without_discount=total_without_discount, gross=gross, discount=discount)
        products = data['products']
        
        for P in products:
            product = Product.objects.get(product_code=P['product_code'])
            product_name = product.name
            price = product.price
            quantity = P['quantity']
            tax = product.tax
            orderline = OrderLines.objects.create(order_no=order, product_code=product, product_name=product_name, price=price, quantity=quantity, tax=tax)
            total_without_discount = float(total_without_discount) + (float(orderline.price) * float(orderline.quantity))
            gross = gross + (float(orderline.price) * float(orderline.quantity)) + (float(orderline.price) * float(orderline.quantity) * float(orderline.tax) / 100)
        gross = gross - (gross * float(discount) / 100)
        Order.objects.filter(order_no=order.order_no).update(total_without_discount=total_without_discount, gross=gross)
        return HttpResponse('Order added successfully')
    else:
        return HttpResponse('Invalid request')

def list_order(request):
    if request.method == "GET":
        orders = Order.objects.all()
        return JsonResponse({'orders': list(orders.values())})
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def edit_order_discount(request):
    if request.method == "PUT":
        data = request.body
        data = json.loads(data)
        id = data['order_no']
        discount = data['discount']
        order = Order.objects.get(order_no=id)
        gross = float(order.total_without_discount) - (float(order.total_without_discount) * float(discount) / 100)
        Order.objects.filter(order_no=id).update(discount=discount, gross=gross)
        return HttpResponse('Order discount updated successfully')
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def edit_orderline(request, id):
    if request.method == "PUT":
        data = request.body
        data = json.loads(data)
        orderline = OrderLines.objects.get(id=id)
        order = Order.objects.get(order_no=orderline.order_no.order_no)
        product_code = orderline.product_code
        product = Product.objects.get(product_code=product_code)
        product_name = product.name
        price = product.price
        quantity = data['quantity']
        tax = product.tax
        OrderLines.objects.filter(id=id).update(product_code=product_code, product_name=product_name, price=price, quantity=quantity, tax=tax)
        total_without_discount = 0
        gross = 0
        orderlines = OrderLines.objects.filter(order_no=order)
        for orderline in orderlines:
            total_without_discount = total_without_discount + (orderline.price * orderline.quantity)
            gross = gross + (orderline.price * orderline.quantity) + (orderline.price * orderline.quantity * orderline.tax / 100)
        Order.objects.filter(order_no=order.order_no).update(total_without_discount=total_without_discount, gross=gross)
        return HttpResponse('Orderline updated successfully')
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def delete_orderline(request, id):
    if request.method == "DELETE":
        orderline = OrderLines.objects.get(id=id)
        order = Order.objects.get(order_no=orderline.order_no.order_no)
        OrderLines.objects.filter(id=id).delete()
        total_without_discount = 0
        gross = 0
        orderlines = OrderLines.objects.filter(order_no=order)
        for orderline in orderlines:
            total_without_discount = total_without_discount + (orderline.price * orderline.quantity)
            gross = gross + (orderline.price * orderline.quantity) + (orderline.price * orderline.quantity * orderline.tax / 100)
        Order.objects.filter(order_no=order.order_no).update(total_without_discount=total_without_discount, gross=gross)
        return HttpResponse('Orderline deleted successfully')
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def delete_order(request, id):
    if request.method == "DELETE":
        Order.objects.filter(order_no=id).delete()
        return HttpResponse('Order deleted successfully')
    else:
        return HttpResponse('Invalid request')

        
