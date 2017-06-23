from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)

            return redirect('/')  # TODO: Success Redirect somewhere better.

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    django_logout(request)
    return redirect('/')


def register(request):

    if request.method == 'GET':
        form = CustomUserCreationForm()

    elif request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():

            user = form.save(commit=False)

            # Make any last second changes to the user here...
            user.save()

            # welcome email to new user
            send_mail(
                subject='re: Welcome!',
                message='Story making time.',
                from_email='ryhanlon@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            # users password and login
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)

            return redirect('/')  #TODO: Success Redirect somewhere better.

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
