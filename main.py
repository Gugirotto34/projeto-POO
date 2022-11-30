from Cliente import Cliente
from Medicamento import Medicamento

def cadastroCliente(clientes):
    while True:
        buffer=''
        nome, idade,cpf,medicamento=input('digite o nome, a idade, o cpf e o medicamento do cliente (separado por espaços) ').split()
        buffer=Cliente(nome, idade,cpf,medicamento)
        clientes.append(buffer)
        fim=(input('deseja cadastrar mais um cliente? [s/n] '))
        if fim.lower()!='s':
            break
    return clientes
def editCliente(clientes):
    return clientes
def delCliente(clientes):
    deletar=int(input('digite qual entrada voce deseja deletar (ID): '))
    while not 1<=deletar<=len(clientes):
        deletar=int(input('valor invalido, digite novamente qual entrada voce deseja deletar: '))
    del clientes[deletar-1]
    return clientes
def pesquisaCliente(clientes):
    termo=(input('digite o termo da pesquisa '))
    print('')
    for a in range(len(clientes)):
        if clientes[a].get_nome()==termo or clientes[a].get_cpf()==termo or clientes[a].get_idade()==termo or clientes[a].get_medicamento()==termo:
            clientes[a].get_info()
    print('')
def printCliente(clientes):
    print('')
    for a in range(len(clientes)):
        clientes[a].get_info()
    print('')
def cadastroMedic(medic):
    return medic
def editMedic(medic):
    return medic
def delMedic(medic):
    return medic
def pesquisaMedic(medic):
    medicPesq=[]
    return medicPesq
def printMedic(medic):
    variavelSoPanDaErro=0
clientes=list()
medic=list()
while True:
    print(' o que deseja fazer?')
    print('1 - cadastrar')
    print('2 - editar')
    print('3 - pesquisar')
    print('4 - deletar')
    print('5- imprimir dados')
    print('6 - desligar')
    control=int(input()) #controle de qual funcao fazer
    while not 1<=control<=6:
        print('voce digitou um numero inválido, tente novamente')
        print(' o que deseja fazer?')
        print('1 - cadastrar')
        print('2 - editar')
        print('3 - pesquisar')
        print('4 - deletar')
        print('5- imprimir dados')
        print('6 - desligar')
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
        control2=int(input('deseja deletar 1-cliente ou 2- medicamento? '))
        while not 1<=control2<=2:
            print('valor invalido')
            control2=int(input('deseja deletar 1-cliente ou 2- medicamento? '))
        if control2==1:
            clientes=delCliente(clientes)
        elif control2==2:
            medic=delMedic(medic)
    elif control==5:
        control2=int(input('deseja imprimir 1-cliente ou 2- medicamento? '))
        while not 1<=control2<=2:
            print('valor invalido')
            control2=int(input('deseja imprimir 1-cliente ou 2- medicamento? '))
        if control2==1:
            printC=printCliente(clientes)
        elif control2==2:
           printM=delMedic(medic)
    elif control==6:
        desl=input('deseja desligar? [s/n] ')
        if desl.lower()== 's':
            break