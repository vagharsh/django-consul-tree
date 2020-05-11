from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from account.models import Account
from account.forms import AccountAuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()

    context['accounts'] = accounts

    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def check_auto_login(accounts):
    for account in accounts:
        if account.auto_login:
            return account


def login_view(request):
    context = {}
    user = request.user

    # Check the DB if there is a user with auto_login field is true then it will login with that user
    accounts = Account.objects.all()
    auto_login_enabled_user = check_auto_login(accounts)

    if auto_login_enabled_user:
        login(request, auto_login_enabled_user)
        return redirect('home')

    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, 'account/login.html', context)
