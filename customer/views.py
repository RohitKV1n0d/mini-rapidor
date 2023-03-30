import json
import re
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import customer     
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    customers = customer.objects.all()
    return render(request, 'index.html', {'customers': customers})


@csrf_exempt
def add_customer(request):
    if request.method == 'POST':
        json_post_data = request.body
        print(json_post_data)
        data = json.loads(json_post_data)
        customer_code = data['customer_code']
        name = data['name']
        customer.objects.create(customer_code=customer_code, name=name)
        return HttpResponse('Customer added successfully')
    else:
        return HttpResponse('Invalid request')

def view_customer(request):
    customers = customer.objects.all()
    return JsonResponse(list(customers.values()), safe=False)


@csrf_exempt
def edit_customer(request):
    if request.method == 'POST':
        json_put_data = request.body
        data = json.loads(json_put_data)
        id = data['id']
        customer_code = data['customer_code']
        name = data['name']
        customer.objects.filter(id=id).update(customer_code=customer_code, name=name)
        return HttpResponse('Customer updated successfully')
    return HttpResponse('Invalid request')

@csrf_exempt
def delete_customer(request):
    if request.method == 'POST':
        json_delete_data = request.body
        data = json.loads(json_delete_data)
        id = data['id']
        deleted = customer.objects.filter(id=id).delete()
        return HttpResponse('Customer deleted successfully')


    