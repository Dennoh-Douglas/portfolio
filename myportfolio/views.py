from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')

def taxservices(request):
    return render(request, 'tax.html')