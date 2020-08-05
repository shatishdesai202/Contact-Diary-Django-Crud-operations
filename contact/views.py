from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from .models import Conatct
# Create your views here.


def index(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    contact = Conatct.objects.all()
    context = {'form': form, 'contact': contact}
    return render(request, 'contact/home.html', context)


def delete(request, id):
    Conatct.objects.get(pk=id).delete()
    return HttpResponseRedirect('/')


def update(request, id):
    con = Conatct.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=con)
        form.save()
        form = ContactForm()
        return HttpResponseRedirect('/')
    else:
        form = ContactForm(instance=con)

    contact = Conatct.objects.all()
    context = {'form': form, 'contact': contact}
    return render(request, 'contact/home.html', context)


def search(request):
    form = ContactForm()
    if request.method == "GET":
        val = request.GET['sea']
        names = Conatct.objects.filter(name__contains=val)
        phones = Conatct.objects.filter(phone__contains=val)
        emails = Conatct.objects.filter(email__contains=val)
        print(names)
        print(phones)
        print(emails)
        contact = names.union(phones, emails)
    context = {'form': form, 'contact': contact}
    return render(request, 'contact/home.html', context)
