from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)

            return redirect(reverse_lazy('pipeline:index'))

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print('Valid!')
            user = form.save(commit=False)

            password = form.cleaned_data.get('password')
            user.set_password(password)

            user.save()

            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)

            if next:
                return redirect(next)

            return redirect(reverse_lazy('pipeline:index'))

    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)

    return redirect(reverse_lazy('pipeline:index'))
