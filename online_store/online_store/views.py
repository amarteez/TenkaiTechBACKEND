# backend/online_store/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola, Mundo!")
