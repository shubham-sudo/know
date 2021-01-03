from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import CustomUserCreationForm

# Create your views here.

class Register(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'authent/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'authent/register.html', {'form': form})


class Login(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'authent/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        else:
            return render(request, 'authent/login.html', {'form': form})
