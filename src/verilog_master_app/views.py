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

def verilogbasics1(request):
	return render(request, 'articles/verilog-basics-1.html')

def verilog_basics_2(request):
	return render(request,'articles/verilog-basics-2.html')

def digital_basics(request):
    return render(request,'articles/digital-basics.html')

def modules_and_port_mappings(request):
	return render(request, 'articles/modules-and-port-mappings.html')

def gate_level_modelling(request):
	return render(request, 'articles/gate-level-modelling.html')

def behavioral_2(request):
	return render(request,'articles/behavioral-2.html')

def half_adder(request):
	return render(request,'articles/half-adder.html')
<<<<<<< HEAD

def mux(request):
	return render(request,'articles/mux.html')
=======
>>>>>>> ed1cff22d4cc0a4cff09c5474a4b011cf4ed70c6
