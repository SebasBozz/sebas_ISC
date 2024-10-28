from django.shortcuts import render


#constantes con valores 


# Create your views here.
@login_required (login_url='/login') # Correcto decorador
def home_views(request):
    # Tu lógica aquí
    template_name = "index.html"
    return render(request, template_name)
