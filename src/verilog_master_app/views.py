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

def types_of_modelling(request):
	return render(request, 'articles/types_of_modelling.html')

def dataflow_level_modelling(request):
	return render(request, 'articles/dataflow-level-modelling.html')

def gate_level_modelling(request):
	return render(request, 'articles/gate-level-modelling.html')

def behavioral_2(request):
	return render(request,'articles/behavioral-2.html')

def half_adder(request):
	return render(request,'articles/half-adder.html')

def full_adder(request):
	return render(request, 'articles/full-adder.html')

def full_half_adder(request):
	return render(request, 'articles/full-half-adder.html')

def half_subtractor(request):
	return render(request, 'articles/half-subtractor.html')
	
def mux(request):
	return render(request,'articles/mux.html')
def bin_to_bcd(request):
	return render(request,'articles/bin_to_bcd.html')
def bin_to_gray(request):
	return render(request,'articles/bin_to_gray.html')
def bin_to_xs3(request):
	return render(request,'articles/bin_to_xs3.html')
def parity_generator(request):
	return render(request,'articles/parity_generator.html')
