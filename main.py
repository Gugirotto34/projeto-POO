from Cliente import Cliente
from Medicamento import Medicamento


def cadastroCliente(clientes, idC):
    while True:
        buffer = ''
        idC+=1
        nome, idade, cpf, medicamento = input(
            'digite o nome, a idade, o cpf e o medicamento do cliente (separado por espaços) ').split()
        buffer = Cliente(idC,nome, idade, cpf, medicamento)
        clientes.append(buffer)
        fim = (input('deseja cadastrar mais um cliente? [s/n] '))
        if fim.lower() != 's':
            break
    return clientes , idC


def editCliente(clientes):
    print('Alterar informação do cliente')
    idF = int(input('Digite o ID do cliente '))
    flag = False
    for func in clientes:  # percorre a lista de clientes
        if idF == func.get_id():  # busca pelo ID do cliente a ser alterado
                print('Digite as novas informações do cliente')
                nome, idade, cpf, medicamento = input(
                'digite o nome, a idade, o cpf e o medicamento do cliente (separado por espaços) ').split()
                func.set_nome(nome)  
                func.set_cpf(cpf)
                func.set_idade(idade)
                func.set_medicamento(medicamento)

                flag = True
        if flag == False:
            print("ID não encontrado!")
    return clientes

def delCliente(clientes):
    deletar = str(input('digite a id do funcionario que voce quer deletar: '))
    flag = False
    # percorre a lista de funcionários  # percorre a lista de funcionários
    for i, j in enumerate(clientes):
        if deletar == j.get_id():
            clientes.pop(i)
            flag = True
    if flag == False:
        print("Id não cadastrado!")
    return clientes


def pesquisaCliente(clientes):
    termo = (input('digite o termo da pesquisa '))
    print('')
    for a in range(len(clientes)):
        if clientes[a].get_nome() == termo or clientes[a].get_cpf() == termo or clientes[a].get_idade() == termo or clientes[a].get_medicamento() == termo or clientes[a].get_idC()==termo:
            clientes[a].get_info()
        else:
            print('termo não encontrado')
    print('')


def printCliente(clientes):
    print('')
    for a in range(len(clientes)):
        clientes[a].get_info()
    print('')

def cadastroMedic(medic, idM):
    while True:
        buffer = ''
        idM+=1
        nome, validade = input(
            'digite o nome e a validade do medicamento ').split()
        buffer = Medicamento(idM,nome, validade)
        medic.append(buffer)
        fim = (input('deseja cadastrar mais um medicamento? [s/n] '))
        if fim.lower() != 's':
            break
    return medic , idC


def editMedic(medic):
    print('Alterar informação do medicamento')
    idF = int(input('Digite o ID do medicamento '))
    flag = False
    for func in medic:  # percorre a lista de medic
        if idF == func.get_id():  # busca pelo ID do cliente a ser alterado
                print('Digite as novas informações do medicamento')
                nome, validade = input('digite o nome e a validade do medicamento ').split()
                func.set_nome(nome)  
                func.set_validade(validade)
                flag = True
    if flag == False:
        print("ID não encontrado!")
    return medic

def delMedic(medic):
    deletar = str(input('digite a id do medicamento que voce quer deletar: '))
    flag = False
    # percorre a lista de funcionários  # percorre a lista de funcionários
    for i, j in enumerate(medic):
        if deletar == j.get_id():
            medic.pop(i)
            flag = True
    if flag == False:
        print("Id não cadastrado!")
    return medic


def pesquisaMedic(medic):
    termo = (input('digite o termo da pesquisa '))
    print('')
    for a in range(len(medic)):
        if medic[a].get_nome() == termo or medic[a].get_validade() == termo or medic[a].get_idM() == termo :
            medic[a].get_info()
        else:
            print('termo não encontrado')
    print('')


def printMedic(medic):
    print('')
    for a in range(len(medic)):
        medic[a].get_info()
    print('')


clientes = list()
medic = list()
idC=0
idM=0
while True:
    print(' o que deseja fazer?')
    print('1 - cadastrar')
    print('2 - editar')
    print('3 - pesquisar')
    print('4 - deletar')
    print('5- imprimir dados')
    print('6 - desligar')
    control = int(input())  # controle de qual funcao fazer
    while not 1 <= control <= 6:
        print('voce digitou um numero inválido, tente novamente')
        print(' o que deseja fazer?')
        print('1 - cadastrar')
        print('2 - editar')
        print('3 - pesquisar')
        print('4 - deletar')
        print('5- imprimir dados')
        print('6 - desligar')
        control = int(input())
    if control == 1:
        # controle de em qual classe realizar
        control2 = int(input('deseja cadastrar 1-cliente ou 2- medicamento? '))
        while not 1 <= control2 <= 2:
            print('valor invalido')
            control2 = int(
                input('deseja cadastrar 1-cliente ou 2- medicamento? '))
        if control2 == 1:
            clientes,idC = cadastroCliente(clientes,idC)
        elif control2 == 2:
            medic,idM = cadastroMedic(medic,idM)
    elif control == 2:
        control2 = int(input('deseja editar 1-cliente ou 2- medicamento? '))
        while not 1 <= control2 <= 2:
            print('valor invalido')
            control2 = int(
                input('deseja editar 1-cliente ou 2- medicamento? '))
        if control2 == 1:
            clientes = editCliente(clientes)
        elif control2 == 2:
            medic = editMedic(medic)
    elif control == 3:
        control2 = int(input('deseja pesquisar 1-cliente ou 2- medicamento? '))
        while not 1 <= control2 <= 2:
            print('valor invalido')
            control2 = int(
                input('deseja pesquisar 1-cliente ou 2- medicamento? '))
        if control2 == 1:
            clientesPesq = pesquisaCliente(clientes)
        elif control2 == 2:
            medicPesq = pesquisaMedic(medic)
    elif control == 4:
        control2 = int(input('deseja deletar 1-cliente ou 2- medicamento? '))
        while not 1 <= control2 <= 2:
            print('valor invalido')
            control2 = int(
                input('deseja deletar 1-cliente ou 2- medicamento? '))
        if control2 == 1:
            clientes = delCliente(clientes)
        elif control2 == 2:
            medic = delMedic(medic)
    elif control == 5:
        control2 = int(input('deseja imprimir 1-cliente ou 2- medicamento? '))
        while not 1 <= control2 <= 2:
            print('valor invalido')
            control2 = int(
                input('deseja imprimir 1-cliente ou 2- medicamento? '))
        if control2 == 1:
            printC = printCliente(clientes)
        elif control2 == 2:
            printM = printMedic(medic)
    elif control == 6:
        desl = input('deseja desligar? [s/n] ')
        if desl.lower() == 's':
            break
