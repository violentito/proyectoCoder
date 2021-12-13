from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import JugadorFormulario
# Create your views here.
#Primer Vista
def inicio(request):
    #return HttpResponse('Esto es una prueba del inicio')
    return render(request, 'AppCoder/inicio.html')

def jugadores(request):
    
    return render(request, 'AppCoder/jugadores.html')

def profesor(request):
    
    return render(request, 'AppCoder/profesor.html')

def estudiante(request):
    
    return render(request, 'AppCoder/estudiante.html')

def entregable(request):
    
    return render(request, 'AppCoder/entregable.html')

def curso(request):
    
    return render(request, 'AppCoder/curso.html')

def jugadorFormulario(request):
    #obtiene el Apellido y el numero, el boobleano(buscar)
  
    if request.method == 'POST':
        miFormulario = JugadorFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            jugadorInsta = Jugador(apellido=informacion['apellido'], numero=informacion['numero'], esBueno=informacion['esBueno'])
            jugadorInsta.save() #la guarda en db
            return render(request, 'AppCoder/Inicio.html')

    else:
        miFormulario = JugadorFormulario()
    return render(request, 'AppCoder/jugadorFormulario.html', {'miFormulario':miFormulario})

def busquedaNumero(request):
    return render(request, 'AppCoder/busquedaJugador.html')

def buscar(request):
    if request.GET['apellido']:
        
        apellido = request.GET['apellido']
        jugador = Jugador.objects.filter(apellido__incontains=apellido)


        respuesta = f"ESTOY BUSCANDO A: {request.GET['apellido']}"

        return render(request, 'AppCoder/resultadoBusqueda.html', {apellido:})

    else:
        respuesta = f"No puedo buscar"

    return HttpResponse(respuesta)