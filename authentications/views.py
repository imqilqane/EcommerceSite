from django.shortcuts import redirect, render
from .forms import AccountCreationForm, LoginForm
from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def registeration_view(request):
    if request.user.is_authenticated:
        return redirect('products:home')


    form = AccountCreationForm()
    if request.method == 'POST':
        password2 = request.POST.get('password2')
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password2)
            user.save()
    
    context = {
        'form':form
    }

    return render(request, 'authentications/register.html', context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('products:home')

    form = LoginForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
        else:
            raise ValueError('something went wrong')

    context = {
        'form':form
    }

    return render(request, 'authentications/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('auth:login')