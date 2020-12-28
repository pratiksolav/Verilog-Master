from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('form_submit', views.form_submit,name="form_submit"),
    path('intro1/',views.intro1,name="intro1"),
    path('intro2/',views.intro2,name="intro2"),
    path('digital-basics/',views.digital_basics,name="digital_basics"),
<<<<<<< Updated upstream
=======
    path('modules-and-port-mappings/',views.modules_and_port_mappings, name="modules_and_port_mappings"),
    path('behavioral-2/',views.behavioral_2,name="behavioral2"),
>>>>>>> Stashed changes
]
