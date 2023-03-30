from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import product
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def index(request):
    products = product.objects.all()
    return render(request, 'products/index.html', {'products': products})



@csrf_exempt
def add_product(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data)
        product_code = data['product_code']
        name = data['name']
        price = data['price']
        tax = data['tax']
        product.objects.create(product_code=product_code, name=name, price=price, tax=tax)
        return HttpResponse('Product added successfully')
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def list_product(request):
    if request.method == "POST":
        products = product.objects.all()
        return JsonResponse(list(products.values()), safe=False)
        # return JsonResponse({'products': list(products.values())})
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def edit_product(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data)
        print(data)
        id = data['id']
        product_code = data['product_code']
        name = data['name']
        price = data['price']
        tax = data['tax']
        product.objects.filter(id=id).update(product_code=product_code, name=name, price=price, tax=tax)
        return HttpResponse('Product updated successfully')
    else:
        return HttpResponse('Invalid request')

@csrf_exempt
def delete_product(request):
    if request.method == "DELETE":
        data = request.body
        data = json.loads(data)
        id = data['id']
        product.objects.filter(id=id).delete()
        return HttpResponse('Product deleted successfully')
    else:
        return HttpResponse('Invalid request')

