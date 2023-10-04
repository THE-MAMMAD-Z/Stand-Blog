from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages

def index(request):
    context={'title':'MY page'}
    return render(request, 'home/index.html',context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your message set successfully')
            return redirect('/contact/')
    form=ContactForm()     
    return render(request, 'home/contact.html',{'form':form})