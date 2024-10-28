from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import path

# Create your views here.
def login_view(request):
    template_name = "login.html"
    
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')
    
    #autentificación del usuario    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contraseña = formulario.cleaned_data['password']
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                    login(request, user)
                    return redirect('home')
                                
    else:
        messages.error(request, 'Invalid login credentials')
    return render(request, template_name)

#login for registrer 

def register_view(request):
    template_name = "registro.html"
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        print(username)
        print(email)
        print(password)
        print(password_confirmation)
        
        if password != password_confirmation:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, template_name)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe.')
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya existe.')
            return render(request, template_name)
        
        user = User(
            username=username,
            email=email,
            password=make_password(password),
            is_active = 0
        )
        user.save()
        messages.success(request, 'Usuario creado exitosamente.')
        return redirect('login')
    return render(request, template_name=template_name)

#forgot de password 
def forgot_view(request):
    template_name = "forgot.html"
    return render(request, template_name=template_name)

#forgot de logout
def logout_view(request):
    logout(request)
    return redirect('login')
