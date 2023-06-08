from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def user_list(request):
    return render(request, "user_register/user_list.html")

def user_form(request):
    form = UserForm()
    return render(request, "user_register/user_form.html", {'form':form})

def user_delete(request):
    return    