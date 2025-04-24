from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт успешно создан!')
            return redirect('login')  # или 'home', если логина пока нет
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
