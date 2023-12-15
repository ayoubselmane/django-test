from django.shortcuts import render, HttpResponse , redirect
from .models import Receipt
from .forms import ReceiptForm


# this is the view for the page where we list the receipts of each user
# we arent using any landing page so this will be it
def home(request):
    # checking if we came through a GET erquest for a normal redirection
    # or an Edit route with POST request
    if request.method == 'POST':
        if 'submit' in request.POST:
            # filling the INSERT query with the request data
            form = ReceiptForm(request.POST)
            # adding the user data (the user isn't allowed to change who submitted it) and saving it to the database
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

    # quering an updated list of the user's receipts
    data = Receipt.objects.filter(user=request.user.id).values()
    # rendering the html data 
    return render(request, "receipts/list.html",{'data': data})

# the view for adding new receipts
def create_receipt(request):
    # creating a form (django form) for adding new receipts
    form = ReceiptForm()
    # rendering te html data while passing our form as context
    return render(request, "receipts/form.html",{'form':form})

# simply deleting a receipt
def delete_receipt(request, id):
    if request.user.id is None:
        return redirect('home')
    Receipt.objects.get(id=id).delete()
    
    return redirect('home')


# edeting a receipt
def edit_receipt(request, id):
    if request.user.id is None:
        return redirect('home')
    # if not request.user.is_authenticated():
    #     return redirect('home')
    # checking whether this is the edit link in the main page or that of the form page
    if request.method == 'GET':
        # since it is a get request the link of the main page was clicked
        # getting the data of the receipt the user wants to modify
        data = Receipt.objects.get(id=id)
        # filling the edit form with the previous data
        form = ReceiptForm(instance=data)
        # rendering the edit form with the fields filled and passing it as context
        return render(request, "receipts/form.html", {'form': form})
    
    elif request.method == 'POST':
        # checked that we are in the form
        # getting the receipt to be modifed
        data = Receipt.objects.get(id=id)
        # saving the modification on the form 
        form = ReceiptForm(request.POST, instance=data)
        # commiting the changes to the database
        form.save()

        return redirect('home')

def details(request, id):
    if request.user.id is None:
        return redirect('home')
    # getting the receipt the user wants its details 
    data = Receipt.objects.get(id=id)
    # passing the receipt object to the html page as context
    return render(request, "receipts/detail.html", {'data': data})
