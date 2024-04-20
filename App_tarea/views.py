from django.shortcuts import render
from django.http import HttpResponse
from App_tarea.models import Topic, Webpage, AccessRecord, Eras
from . import forms

# Create your views here.
def index(request):
    access_list = AccessRecord.objects.order_by('date')
    eras_list = Eras.objects.order_by('email')
    my_context = {'username': 'Templates y archivos estáticos',
        'access_records' : access_list,'eras_l': eras_list,
        'libros': ['Orgullo y Prejuicio', 'Divine Rivals', 'Once Upon a Broken Heart'],
        'taylor_swift': ['Folklore', 'Midnights', '1989'],
        'cafe': 'Amo el café en cualquier presentación'}
    return render(request, 'App_tarea/index.html', context=my_context)
    
    #Crear un formulario para mostrar
def form_user_view(request):
    form = forms.FormUser()
    return render(request, 'mi_primera_app/form_page.html', {'form' : form})