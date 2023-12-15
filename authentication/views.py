from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# logging user in
def login_user(request):
    if request.method == 'POST':
        # getting the form data submitted by the user
        username = request.POST['username']
        password = request.POST['password']
        # checking if the user credentials are correct and fetching a user 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if the user indeed has an account we log him in and send him to te home page
            login(request, user)
            return redirect('home')
        else:
            # if the user doesnt have an account we send him back to the login page with a message 
            messages.success(request, ('It seems like either your username or your password is wrong'))
            return redirect('login')
    
    return render(request,"authentication/login.html")

# simply logging the user out and redirecting him to the home page
def logout_user(request):
    logout(request)
    messages.success(request,('You were logged out successfully'))
    return redirect('home')

# creating a user account
def register_user(request):
    if request.method == 'GET':
        # assigning the creating account form
        form = UserCreationForm()

    elif request.method == 'POST':
        # filling the form with the request data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if the form was valid we save the new user
            form.save()
            # getting the new user username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # here is the same login process with the new user
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,('Successfully registered'))
            return redirect('home')


    return render(request, "authentication/register.html", {'form':form})