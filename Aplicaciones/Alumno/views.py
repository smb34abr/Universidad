from django.shortcuts import render

# Create your views here.
def Alumno(request):    
    return render(request, 'gestionAlumnos.html')
    