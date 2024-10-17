from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def work(request):
    return render(request, 'work.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def form(request):
    try:
        n1=request.POST['email']
        n2=request.POST.get('password')
        print(n1,n2)

        return HttpResponseRedirect('/')
    except:
        pass
    return render(request, 'form.html')


def calc(request):
    try:
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        n3=None
        operator=request.POST['operator']
        if operator=='add':
            n3=n1+n2
        elif operator=='subtract':
            n3=n1-n2
        elif operator=='multiply':
            n3=n1*n2
        elif operator=='divide':
            n3=n1/n2
        return render(request, 'calculator.html', {'result':n3})
    except:
        pass
    return render(request, 'calculator.html')

