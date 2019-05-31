from django.shortcuts import render, redirect
from django.views.generic import ListView,TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, JustificativaForm
from .models import *
from datetime import datetime, timedelta
import socket
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.


def ValidaHorario(horario1,horario2,tolerancia):
    hora1=horario1.split(':')
    hora2=horario2.split(":")
    h=int(hora1[0])-int(hora2[0])
    m=int(hora1[1])-int(hora2[1])
    h=abs(h)*60+abs(m)
    print(h,':',m)
    if h>= int(tolerancia):
        print(h)
        print(tolerancia)
        return True
    else:
        return False

def Registro(id):
    id=int(id)
    data_atual = datetime.now()
    hora_em_texto = data_atual.strftime('%H:%M:%S')
    data_em_texto=data_atual.strftime('%Y-%m-%d')
    funcionario1=Funcionario.objects.get(usuario__id__exact=id)
    idFuncionario=funcionario1.id
    frequen=Frequencia.objects.filter(fucionario__id__exact=idFuncionario)
    frequencias=None
    a=funcionario1.config_horario
    tolerancia=a.tolerancia
    for i in frequen:
        if str(i.data) == data_em_texto:
            frequencias=i
    if frequencias == None:
        frequencias=Frequencia(data=data_em_texto,fucionario=funcionario1,ipCom=socket.gethostbyname(socket.gethostname()))
        frequencias.status=status.objects.get(id__exact=1)
    if frequencias.horario_entrada_1 == None:
        frequencias.horario_entrada_1=hora_em_texto
        if ValidaHorario(hora_em_texto,str(a.horario_entrada_1),tolerancia):
            frequencias.status=status.objects.get(id__exact=2)
    elif frequencias.horario_saida_1 == None:
        frequencias.horario_saida_1=hora_em_texto
        if ValidaHorario(hora_em_texto,str(a.horario_saida_1),tolerancia):
            frequencias.status=status.objects.get(id__exact=2)
    elif frequencias.horario_entrada_2 == None:
        frequencias.horario_entrada_2=hora_em_texto
        if ValidaHorario(hora_em_texto,str(a.horario_entrada_2),tolerancia):
            frequencias.status=status.objects.get(id__exact=2)
    elif frequencias.horario_saida_2 == None:
        frequencias.horario_saida_2=hora_em_texto
        if ValidaHorario(hora_em_texto,str(a.horario_saida_2),tolerancia):
            frequencias.status=status.objects.get(id__exact=2)
    frequencias.save()
    return None

@login_required(login_url='http://localhost:8000/login/ponto')
def login_sucesso(request):
    usuario=request.user
    print(usuario)
    return render(request, 'app_ponto/login_sucesso.html',{'usuario':usuario})

def logout_user(request):
    logout(request)
    return redirect("http://localhost:8000/login/ponto")

def user_login(request,ponto):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('Senha')
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            if user.is_active:
                print(user.id)
                login(request, user)
                id=user.id
                if ponto =="ponto":
                    Registro(user.id)
                    return redirect(login_sucesso)
                else:
                    return redirect('http://localhost:8000/area/admin/'+str(id))
            else:
                return HttpResponse("Usuário desativado")
                # Retorna uma mensagem de erro de 'conta desabilitada' .
        else:
            messages.error(request,'Login ou senha invalidos. Tente Novamente')
            # Retorna uma mensagem de erro 'login inválido'.
    else:
        form = LoginForm()
    if ponto =="ponto":
        return render(request, 'app_ponto/login.html', {'form': form})
    else:
        return render(request, 'app_ponto/loginAreaR.html', {'form': form})

@login_required(login_url='http://localhost:8000/')
@permission_required('Can add frequencia',login_url='http://localhost:8000/login/conta/admin')
def FrequenciaFuncionario(request,idF):
    funcionario1=Funcionario.objects.get(usuario__id__exact=idF)
    idSupervisor=funcionario1.id
    subordinados=Funcionario.objects.filter(supervisor__id__exact=idSupervisor)
    frequencias=Frequencia.objects.filter(fucionario__supervisor__id__exact=idSupervisor)
    return render(request, 'app_ponto/areaAdmin.html', {'frequencias': frequencias,"funcionario1":funcionario1})

def RegistroJust(just,id):
    funcionario1=Funcionario.objects.get(usuario__id__exact=id)
    print(id)
    idFuncionario=funcionario1.id
    frequen=Frequencia.objects.filter(fucionario__id__exact=idFuncionario)
    data_atual = datetime.now()
    data_em_texto=data_atual.strftime('%Y-%m-%d')
    for i in frequen:
        if str(i.data) == data_em_texto:
            i.justificativa=just
            i.save()

def CadastroJust(request):
    if request.method == "POST":
        form=JustificativaForm(request.POST)
        if form.is_valid():  
            form.save()
            justificativas=Justificativa.objects.all()
            x=len(justificativas)-1
            usuario=request.user
            id=usuario.id
            RegistroJust(justificativas[x],id)
            return redirect('login_sucesso')
    else:
        form=JustificativaForm()
    return render (request,'app_ponto/CadastroFre.html',{'form':form})