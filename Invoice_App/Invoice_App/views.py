from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from inventory.models import Inventory
from inventory.forms import InventoryUpdateForm
from invoice.models import Invoice, Product
from invoice.forms import InvoiceForm
from decimal import Decimal


def mainpage(request):
    return render(request,'mainpage.html')

def welcome(request):#error logout
	return render(request,'welcome.html')

#new user signup funtion
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        my_user.save()
        return redirect('login')
    return render(request,"signup.html")

#login user function       
def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/welcome/')
		else:
			return HttpResponse('incorrect')
	return render(request,'login.html')

#this is a logout function
def logout(request):
	logout(request)
	return redirect('login')

#this function add new item and show all item
def inventory(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        company = request.POST.get('company')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        # Create an instance of the Inventory model and save it
        my_data = Inventory(product_name=product_name, company=company, quantity=quantity, price=price)
        my_data.save()
        messages.success(request, "Successfully saved")
        return redirect('inventory')
    else:
        invent = Inventory.objects.all()
    return render(request, 'inventory.html', {'invs': invent})

#this function will delete item
def delete(request, id):
    if request.method =='POST':
        pi=Inventory.objects.get(pk=id)
        pi.delete()
        return redirect('inventory')

#this function will update item
def update(request, id):
    pi = get_object_or_404(Inventory, pk=id)
    if request.method == 'POST':
        fm = InventoryUpdateForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('inventory') 
    else:
        fm = InventoryUpdateForm(instance=pi)
    return render(request, 'update.html', {'form': fm, 'pi': pi})

def billing(request):
    data = Inventory.objects.all()
    return render(request,'billing.html',{
        'inventory':data
    })

def gen_pdf(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_gst = request.POST.get('customer_gst')
        phone = request.POST.get('phone')
        product_name = request.POST.getlist('product_name')
        quantity = request.POST.getlist('quantity')
        price = request.POST.getlist('price')
        total = []  
        netamount = Decimal(0)
        date = request.POST.get('date')

        for i in range(len(product_name)):
            product_total = Decimal(quantity[i]) * Decimal(price[i])
            total.append(product_total)
            netamount += product_total
            
            # Fetch the inventory item for the product
            inventory_item = Inventory.objects.get(product_name=product_name[i])
            # Convert the inventory quantity to an integer
            inventory_quantity = int(inventory_item.quantity)
            # Check if there's enough inventory for the sale
            if inventory_quantity >= int(quantity[i]):
                # Update the inventory quantity
                inventory_item.quantity -= int(quantity[i])
                inventory_item.save()
            else:
                # Handle the case where there's not enough inventory
                messages.error(request, f"Not enough inventory for {product_name[i]}")
                return redirect('billing')
        invoice = Invoice.objects.create(
            customer_name=customer_name,customer_gst=customer_gst,phone=phone,
            product_name=product_name,quantity=quantity,price=price,total=total,netamount=netamount,date=date 
        )
        for i in range(len(product_name)):
            Product.objects.create(
                invoice=invoice,
                product_name=product_name[i],
                quantity=quantity[i],
                price=price[i],
                total=total[i],
                netamount=total[i] 
            )
        messages.success(request, "Successfully saved")
        return render(request, 'pdf.html', {'invo': invoice})
    return render(request, 'billing.html')


def orderhistory(request):
    customer_name = Invoice.objects.all()
    context={
        'customer_name': customer_name,
    }
    return render(request,'orderhistory.html',context)


def view(request, id):
    customer = Invoice.objects.get(id=id)
    if request.method == 'POST':
        fm = InvoiceForm(request.POST, instance=customer)
        if fm.is_valid():
            fm.save()
            return redirect('orderhistory')
    else:
        fm = InvoiceForm(instance=customer)
    return render(request, 'view.html', {'form': fm, 'pi': customer,'ps': customer.invoice.all()})






