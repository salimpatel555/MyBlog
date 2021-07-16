from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from.models import Product
from.forms import ProductForm
# Create your views here.
def product(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'product.html',context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        form = ProductForm()  
        context = {'form':form}      
    return render(request,'add_product.html',context)

def edit_product(request,id):
    if request.method =='POST':
        product = Product.objects.get(pk=id)
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        product = Product.objects.get(pk=id)
        form = ProductForm(instance=product)    
    return render(request,'edit_product.html',{'form':form})  

def delete_product(request,id):
    if request.method=='POST':
        product = Product.objects.get(id=id)
        product.delete() 
        return HttpResponseRedirect('/product')       