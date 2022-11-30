from Cliente import Cliente
from Medicamento import Medicamento

def cadastroCliente(clientes):
    return clientes
def editCliente(clientes):
    return clientes
def delCliente(clientes):
    return clientes
def pesquisaCliente(clientes):
    clientesPesq=[]
    return clientesPesq
def cadastroMedic(medic):
    return medic
def editMedic(medic):
    return medic
def delMedic(medic):
    return medic
def pesquisaMedic(medic):
    medicPesq=[]
    return medicPesq
clientes=list()
medic=list()
while True:
    print(' o que deseja fazer?')
    print('1 - cadastrar')
    print('2 - editar')
    print('3 - pesquisar')
    print('4 - deletar')
    print('5 - desligar')
    control=int(input()) #controle de qual funcao fazer
    while not 1<=control<=5:
        print('voce digitou um numero inválido, tente novamente')
        print(' o que deseja fazer?')
        print('1 - cadastrar')
        print('2 - editar')
        print('3 - pesquisar')
        print('4 - deletar')
        print('5 - desligar')
        control=int(input())
    if control == 1:
        control2=int(input('deseja cadastrar 1-cliente ou 2- medicamento? ')) #controle de em qual classe realizar
        while not 1<=control2<=2:
            print('valor invalido')
            control2=int(input('deseja cadastrar 1-cliente ou 2- medicamento? '))
        if control2==1:
            clientes=cadastroCliente(clientes)
        elif control2==2:
            medic=cadastroMedic(medic)
    elif control ==2:
        control2=int(input('deseja editar 1-cliente ou 2- medicamento? '))
        while not 1<=control2<=2:
            print('valor invalido')
            control2=int(input('deseja editar 1-cliente ou 2- medicamento? '))
        if control2==1:
            clientes=editCliente(clientes)
        elif control2==2:
            medic=editMedic(medic)
    elif control==3:
        control2=int(input('deseja pesquisar 1-cliente ou 2- medicamento? '))
        while not 1<=control2<=2:
            print('valor invalido')
            control2=int(input('deseja pesquisar 1-cliente ou 2- medicamento? '))
        if control2==1:
            clientesPesq=pesquisaCliente(clientes)
        elif control2==2:
            medicPesq=pesquisaMedic(medic)
    elif control==4:
        control2=int(input('deseja editar 1-cliente ou 2- medicamento? '))
        while not 1<=control2<=2:
            print('valor invalido')
            control2=int(input('deseja editar 1-cliente ou 2- medicamento? '))
        if control2==1:
            clientes=editCliente(clientes)
        elif control2==2:
            medic=editMedic(medic)
    elif control==5:
        desl=input('deseja desligar? [s/n] ')
        if desl.lower()== 's':
            break