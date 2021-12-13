from django.urls import path
from AppCoder import views

urlpatterns = [

    
    path('inicio', views.inicio, name="Inicio"),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('estudiante', views.estudiante, name="Estudiante"),
    path('profesor', views.profesor, name="Profesor"),
    path('entregable', views.entregable, name="Entregable"),
    path('curso', views.curso, name="Curso"),
    path('jugadorFormulario', views.jugadorFormulario, name="JugadorFormulario"),
    path('busquedaJugador', views.busquedaNumero, name="BusquedaJugador"),
    path('buscar', views.buscar),

]
