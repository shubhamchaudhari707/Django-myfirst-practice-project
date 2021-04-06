from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User

from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Crudproject
from django.contrib import messages

# Create your views here.


def check_admin(user):
    return user.is_superuser


@login_required(login_url='/')
def home(request):
    return render(request, 'testapp/home.html')


def signup_user(request):
    if request.method == 'POST':
        nm = request.POST['first_name']
        lm = request.POST['last_name']
        em = request.POST['email']
        us = request.POST['username']
        pw1 = request.POST['Password1']
        pw2 = request.POST['Password2']

        if pw1 == pw2:
            if User.objects.filter(username=us).exists():
                messages.info(request, 'username already taken !!')
                return redirect('signup')
            elif User.objects.filter(email=em).exists():
                messages.info(request, 'email already taken !!')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=nm, last_name=lm, email=em, username=us, password=pw1)
                user.save()
                print('user created')
                messages.info(request, 'Signup Created Successfully !!')
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching!!')
            return redirect('signup')
    else:
        return render(request, 'testapp/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # print(user.is_superuser)

        if user is None:
            messages.info(request, 'invailid credentials ')
            return redirect('login')

        else:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('home')
    else:
        return render(request, 'testapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='/')
@user_passes_test(check_admin, login_url='/')
def admin_user(request):
    use = User.objects.exclude(id=request.user.id)
    return render(request, 'testapp/admin.html', {'us': use})


@login_required(login_url='/')
def crud(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        marks = request.POST['marks']
        cru = Crudproject(name=name, subject=subject, marks=marks, user=request.user)
        cru.save()
        messages.info(request, 'Sucessfully')
        return redirect('crud')
    else:
        stud = Crudproject.objects.filter(user=request.user)
        return render(request, 'testapp/crud.html', {'student': stud})


def Delete(request, id):
    if request.method == 'POST':
        pi = Crudproject.objects.get(pk=id)
        pi.delete()
        return redirect('crud')


def update_data(request, id):
    pi = Crudproject.objects.get(pk=id)
    if request.method == 'POST':
        pi.name = request.POST['name']
        pi.subject = request.POST['subject']
        pi.marks = request.POST['marks']
        pi.save()
        return redirect('crud')
    else:
        return render(request, 'testapp/updates.html', {'data': pi})


