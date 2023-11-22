from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.views.generic import ListView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Poliza,Auto,Contacto,UserExtension
from .forms import PolizaForm,AutoForm,FormularioRegistroUsuario,FormContacto,FormCambioPassword,Formperfiledit
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, "IturbeSeguros.html")

def acercademi(request):
    return render(request, "Acercademi.html")

@login_required
def imagenavatar(request):
    if request.method == 'POST':
        formava = Formperfiledit(request.POST, request.FILES)

        if formava.is_valid():
            datos_perfil = formava.cleaned_data

            request.user.email = datos_perfil['email']
            request.user.first_name = datos_perfil['first_name']
            request.user.last_name = datos_perfil['last_name']


            if datos_perfil['avatar'] == False:
                request.user.userextension.avatar = None
            elif datos_perfil['avatar'] != None:
                request.user.userextension.avatar = datos_perfil['avatar']

            request.user.userextension.descripcion = datos_perfil['descripcion']
            request.user.userextension.link = datos_perfil['link']
                    
            request.user.save()
            request.user.userextension.save()

            return redirect('perfil')
    else:
        formava = Formperfiledit(
            initial={
                'email' : request.user.email,
                'first_name' : request.user.first_name,
                'last_name' : request.user.last_name,
                'avatar' : request.user.userextension.avatar,
                'descripcion' : request.user.userextension.descripcion,
                'link' : request.user.userextension.link,
            }
        )
    return render(request, 'editar_perfil.html', { 'formava' : formava })
@login_required
def form_poliza(request):
    if request.method == "POST":
        form1 = PolizaForm(request.POST,request.FILES)
        if form1.is_valid():
            poliza = form1.save()
            return redirect("poliza")
    else:
        form1= PolizaForm
    return render (request,"crear_poliza.html",{"form1": form1})
@login_required
def poliza(request):
    return render(request,"poliza.html")
@login_required
def Perfil(request):
    return render(request,"perfil.html")

@login_required
def buscador(request):

    categoria = request.GET.get("categoria")

    if categoria:

        polizas=Poliza.objects.filter(categoria__icontains= categoria)
        return render(request,"buscador.html",{"polizas": polizas, "categoria": categoria})
    
    else:
        respuesta= "No enviaste Datos"

    return render(request,"buscador.html",{"respuesta": respuesta})
@login_required
def auto(request):
    return render(request,"auto.html")

class Autoview(LoginRequiredMixin,ListView):
    model=Auto
    template_name ="buscar_auto.html"
    context_object_name = "autos"

class Autodelete(LoginRequiredMixin,DeleteView):
    model=Auto
    template_name= "Auto_confirm.html"
    success_url= reverse_lazy("auto")

class autoupdate(LoginRequiredMixin,UpdateView):
    model= Auto
    template_name="editar_auto.html"
    form_class = AutoForm
    success_url= reverse_lazy("auto")
@login_required
def form_auto(request):

    if request.method == "POST":
        formuauto= AutoForm(request.POST, request.FILES)
        if formuauto.is_valid():
            auto= formuauto.save()
            return redirect("auto")
    else:
        formuauto= AutoForm
    return render (request,"crear_auto.html",{"formuauto": formuauto})
@login_required
def buscar_auto(request):
    
    placa = request.GET.get("placa")

    if placa:

        placas=Auto.objects.filter(placa__icontains= placa)
        return render(request,"buscar_auto.html",{"placas":placas,"placa": placa})
    
    else:
        respuesta= "No enviaste Datos"

    return render(request,"buscar_auto.html",{"respuesta": respuesta})

class Polizalistviewt(ListView):
    model= Poliza
    template_name = "buscador.html"
    context_object_name= "poliza"

class PolizaDelete(DeleteView):
    model=Poliza
    template_name= "poliza_confirm.html"
    success_url= reverse_lazy("poliza")

class Polizaupteview(UpdateView):
    model= Poliza
    template_name="editar_poliza.html"
    form_class = PolizaForm
    success_url= reverse_lazy("poliza")

def user_login(request):
    if request.method == "POST":
        form_login= AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            user_extension,nuevo_userextension = UserExtension.objects.get_or_create(user=request.user)
            return redirect("IturbeSeguros")
        else:
            form_login= AuthenticationForm
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request,"login.html")

@login_required
def user_logout(request):
    logout(request)
    return render(request,"logout.html")

def user_register(request):
    if request.method == "POST":
        form = FormularioRegistroUsuario(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("user_login")  
    else:
        form = FormularioRegistroUsuario()
    return render(request,'register.html', {'form': form})

def contactoview(request):
    if request.method == "POST":
        form = FormContacto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("envioform")  
    else:
        form = FormContacto()
    return render(request,'Contacto.html', {'form': form})

def envioform1(request):
    return render(request, "formenviado.html")

class CambioPassword(LoginRequiredMixin,PasswordChangeView):
    form_class = FormCambioPassword
    template_name = 'changepass.html'
    success_url = reverse_lazy('passcambiadoexitoso')

def password_exitoso(request):
    return render(request, 'passcambiadoexitoso.html')