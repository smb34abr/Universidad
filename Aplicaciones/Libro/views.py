from django.shortcuts import render

# Create your views here.
def libro(request):
    return render(request, 'gestionLibros.html')
