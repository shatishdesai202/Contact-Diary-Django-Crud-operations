from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from .models import Conatct
from django.contrib import messages

# Authentication

# from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, User

# form import
from .forms import SignupForm, LoginForm


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'Successfully Logout')
        return HttpResponseRedirect('/login/')
    else: 
        return HttpResponseRedirect('/login/')


def login_(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upassword = form.cleaned_data['password']
            user = authenticate(username=uname, password=upassword)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'contact/login.html', context)


def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignupForm()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'contact/signup.html', context)


def index(request, id=None):
    # ip = request.session['ip']
    if id == None:
        if request.user.is_authenticated:
            contact = Conatct.objects.filter(contact_of=request.user)
            if request.method == "POST":

                form = ContactForm(request.POST, request.FILES)
                if form.is_valid():
                    inst = form.save(commit=False)
                    inst.contact_of = request.user
                    inst.save()
                    return HttpResponseRedirect('/')
            else:

                form = ContactForm()

        else:
            contact = None
            return HttpResponseRedirect('/login/')
        context = {'form': form, 'contact': contact}
        return render(request, 'contact/home.html', context)
    else:
        con = Conatct.objects.get(pk=id)
        if request.method == "POST":
            form = ContactForm(request.POST, instance=con)
            if form.is_valid():
                form.save()
                messages.info(request, f'Updated : {con.name}')
                return HttpResponseRedirect('/')
        else:
            
            form = ContactForm(instance=con)

        contact = Conatct.objects.filter(contact_of=request.user)
        context = {'form': form, 'contact': contact, 'ip':ip}
        return render(request, 'contact/home.html', context)


def delete(request, id):
    contactn = Conatct.objects.get(pk=id)
    messages.error(request, f'Deleted : {contactn.name}')
    contactn.delete()
    return HttpResponseRedirect('/')


def search(request):
    form = ContactForm()
    if request.method == "GET":
        val = request.GET['sea']
        names = Conatct.objects.filter(
            name__contains=val, contact_of=request.user)
        phones = Conatct.objects.filter(
            phone__contains=val, contact_of=request.user)
        emails = Conatct.objects.filter(
            email__contains=val, contact_of=request.user)
        
        contact = names.union(phones, emails)
        context = {'contact': contact, 'form': form}

    else:
        if request.user.is_authenticated:
            contact = Conatct.objects.filter(contact_of=request.user)
            if request.method == "POST":

                form = ContactForm(request.POST, request.FILES)
                if form.is_valid():
                    inst = form.save(commit=False)
                    inst.contact_of = request.user
                    inst.save()
                    return HttpResponseRedirect('/')
            else:

                form = ContactForm()

        else:
            contact = None
            return HttpResponseRedirect('/login/')
        context = {'form': form, 'contact': contact}
        return render(request, 'contact/home.html', context)
    return render(request, 'contact/home.html', context)
