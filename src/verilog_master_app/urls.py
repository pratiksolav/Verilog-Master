from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('form_submit', views.form_submit,name="form_submit"),
    path('intro1/',views.intro1,name="intro1"),
    path('intro2/',views.intro2,name="intro2"),
    path('verilog-basics-1/',views.verilogbasics1, name="verilogbasics1"),
    path('verilog-basics-2/',views.verilog_basics_2, name="verilog_basics_2"),
    path('digital-basics/',views.digital_basics,name="digital_basics"),
    path('modules-and-port-mappings/',views.modules_and_port_mappings, name="modules_and_port_mappings"),
    path('types_of_modelling/',views.types_of_modelling,name="types_of_modelling"),
    path('gate-level-modelling/',views.gate_level_modelling, name="gate_level_modelling"),
    path('dataflow_level_modelling/',views.dataflow_level_modelling, name="dataflow_level_modelling"),
    path('behavioral-2/',views.behavioral_2,name="behavioral2"),
    path('half-adder/',views.half_adder,name="half_adder"),
    path('full-adder/',views.full_adder,name="full_adder"),
    path('full-half-adder/',views.full_half_adder,name="full_half_adder"),
    path('half-subtractor/',views.half_subtractor,name="half_subtractor"),
    path('mux/',views.mux,name="mux"),
    path('bin_to_bcd/',views.bin_to_bcd,name="bin_to_bcd"),
    path('bin_to_gray/',views.bin_to_gray,name="bin_to_gray"),
    path('bin_to_xs3/',views.bin_to_xs3,name="bin_to_xs3"),
    path('parity_generator/',views.parity_generator,name="parity_generator"),

]
