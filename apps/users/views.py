from django.shortcuts import render, redirect
from apps.users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def main(req):
    return render(req, "users/main.html")

def signup(req):
    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth.login(req,user)
            return redirect('users:main')
        else:
            ctx = {
                'form': form,
            }
            return render(req, 'users/signup.html')
    else:
        form = SignupForm()
        ctx = {
            'form': form,
        }
        return render(req, template_name = 'users/signup.html', context=ctx)
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
