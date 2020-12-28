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
		return render(request,'articles/home.html')

def intro1(request):
    return render(request,'articles/intro1.html')

def intro2(request):
    return render(request,'articles/intro2.html')

<<<<<<< Updated upstream
def digital_basics(request):
    return render(request,'digital-basics.html')
=======
def verilogbasics1(request):
	return render(request, 'articles/verilog-basics-1.html')

def digital_basics(request):
    return render(request,'articles/digital-basics.html')

def verilog_basics_1(request):
	return render(request,'articles/verilog-basics-1.html')

def verilog_basics_2(request):
	return render(request,'articles/verilog-basics-2.html')

def modules_and_port_mappings(request):
	return render(request, 'articles/modules-and-port-mappings.html')

def behavioral_2(request):
	return render(request,'articles/behavioral-2.html')
>>>>>>> Stashed changes
