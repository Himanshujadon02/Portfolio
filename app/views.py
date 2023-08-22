from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home.html')

def portfolio(request):
   return render(request,'portfolio.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def detail(request):
    return render(request,'detail.html')