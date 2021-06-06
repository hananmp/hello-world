from . models import Products
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    Products_objects = Products.objects.all()

    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        Products_objects = Products_objects.filter(title__icontains = item_name)

    #paginator code
    paginator = Paginator(Products_objects,8)
    page = request.GET.get('page')
    Products_objects = paginator.get_page(page)

    return render(request,'index.html',{'Product_objects': Products_objects}) 
     
def detail(request,id):
    Products_objects = Products.objects.get(id=id)
    return render(request,'detail.html',{'Product_objects':  Products_objects})