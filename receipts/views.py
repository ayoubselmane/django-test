from django.shortcuts import render, HttpResponse , redirect
from .models import Receipt
from .forms import ReceiptForm

def home(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = ReceiptForm(request.POST)
            form.save()
    
    data = Receipt.objects.all().values()

    return render(request, "receipts/list.html",{'data': data})

def create_receipt(request):
    form = ReceiptForm()
    
    return render(request, "receipts/form.html",{'form':form})

def delete_receipt(request, id):
    Receipt.objects.get(id=id).delete()
    
    return redirect('home')

def edit_receipt(request, id):
    if request.method == 'GET':
        data = Receipt.objects.get(id=id)
        form = ReceiptForm(instance=data)
        return render(request, "receipts/form.html", {'form': form})
    
    elif request.method == 'POST':
        data = Receipt.objects.get(id=id)
        form = ReceiptForm(request.POST, instance=data)
        form.save()
        return redirect('home')

def details(request, id):
    data = Receipt.objects.get(id=id)
    return render(request, "receipts/detail.html", {'data': data})
