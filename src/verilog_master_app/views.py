from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def home(request):
	return render(request,'home.html')

def form_submit(request):
	if request.method == 'POST':
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		subject = request.POST.get('subject','')
		message = request.POST.get('message','')
		saveInfo = Contact(name = name,email = email,subject = subject,message = message)
		saveInfo.save()
		return HttpResponse('')
	else:
		render(request,'home.html')

def intro1(request):
    return render(request,'intro1.html')

def intro2(request):
    return render(request,'intro2.html')

def verilogbasics1(request):
	return render(request, 'verilog-basics-1.html')

def digital_basics(request):
    return render(request,'digital-basics.html')
