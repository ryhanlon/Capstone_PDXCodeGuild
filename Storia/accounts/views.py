from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

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
    return render(request, 'accounts/login_user.html', context)


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


@login_required(login_url='/accounts/login/')
def profile(request):
    """
    Log-in to update profile.

    """

    if request.method == 'GET':
        form = CustomUserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    elif request.method == 'POST':
        form = CustomUserUpdateForm(data=request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    context = {'form': form, 'password_form': password_form}
    return render(request, 'accounts/profile.html', context)
