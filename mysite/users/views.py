from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome {username}, your account is created')
            return redirect('login')
    return render (request, 'users/register.html',{'form':form})

@login_required
def profilePage(request):
    return render(request, 'users/profile.html')