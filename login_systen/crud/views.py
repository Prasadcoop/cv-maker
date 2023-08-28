from django.shortcuts import HttpResponse, render ,redirect
from django.template import loader
from .models import Product

# Create your views here.
# def index(request):
#     if request.method =="POST":
#         NAME = request.POST.get('name')
#         TYPE = request.POST.get('type')
#         CATEGORY =request.POST.get('category')
#         PRICE = request.POST.get('price')
#         QUANTITY = request.POST.get('quantity')

#         data = Product(name =Name,ptype= TYPE, category=CATEGORY,price=PRICE,quantity=QUANTITY)
#         data.save()

#     template = loader.get_template(request,'additem.html')
#     return HttpResponse(template.render())

def index(request):

    if request.method =="POST":

        NAME = request.POST.get('name')
        TYPE = request.POST.get('type')

        CATEGORY =request.POST.get('category')
        PRICE = request.POST.get('price')
        QUANTITY = request.POST.get('quantity')

        product=Product.objects.create(name=NAME,Ptype=TYPE,category=CATEGORY,price=PRICE,quantity=QUANTITY)
        p=product.save()
        
        try:
            return HttpResponse("success..")
        except Exception as e:
            return HttpResponse("Error: {str(e)}")
           
         

    return render(request,'additem.html')

def showdetails(request):
    totaldata= Product.objects.all()
    return render(request ,'showdetails.html',{'datatotal':totaldata})

def edit(request,id):
    product = Product.objects.get(id=id)
    return render(request ,'edit.html',{'product':product})
    # return HttpResponse(product)

def update(request ,id):
    
    if request.method == "POST":
        P_ID =request.POST.get('id')
        NAME = request.POST.get('name')
        PTYPE = request.POST.get('Ptype')
        CATEGORY = request.POST.get('category')
        PRICE = request.POST.get('price')
        QUANTITY = request.POST.get('quantity')

        product = Product.objects.get(id=id)
        product.id = P_ID 
        product.name = NAME
        product.Ptype = PTYPE
        product.category = CATEGORY
        product.price = PRICE
        product.quantity = QUANTITY
        s=product.save()
         
        # if s==True:
        #     return redirect('showdata/')
        return redirect('/showdata/')
    # return render(request ,'edit.html',{'product':product})

def Delete(request ,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('/showdata/')