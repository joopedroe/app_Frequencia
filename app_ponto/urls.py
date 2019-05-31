from django.urls import path
from . import views
from app_ponto.views import *

from django.contrib.auth import views as auth_views



urlpatterns=[
    #path('',Registro,name='encontratag'),
    path('login/sucesso/',login_sucesso, name='login_sucesso'),
    path('<str:ponto/>',user_login,name="login_inicial"),
    path('login/<str:ponto>',user_login,name='login'),
    path('sair/',logout_user,name='logout'),
    path('area/admin/<int:idF>/', FrequenciaFuncionario,name='fequenciaFuncionario'),
    path('login/conta/<str:ponto>',user_login,name='login'),
    path('nova/cadastro/<int:id>',CadastroJust,name='CadastroJust'),
]