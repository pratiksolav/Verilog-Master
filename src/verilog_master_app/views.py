from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def intro1(request):
    return render(request,'intro1.html')

def intro2(request):
    return render(request,'intro2.html')
