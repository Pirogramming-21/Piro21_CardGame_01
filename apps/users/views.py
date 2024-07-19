from django.shortcuts import render, redirect
from users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def main(req):
    return render(req, "users/main.html")

def login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(req, user)
            return redirect('users:main')
        else:
            context = {
                'form':form,
            }
            return render(req,template_name='users/login.html',context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(req, template_name='users/login.html', context=context)

def logout(req):
    auth.logout(req)
    return redirect('users:main')

def signup(req):
    pass