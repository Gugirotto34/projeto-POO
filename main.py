from Cliente import Cliente
from Perfume_Medicamento import Medicamento
from ClienteFisico import ClienteFisico
from ClienteJuridico import ClienteJuridico
from Perfume_Medicamento import Perfume


def cadastroCliente(clientes, idC):
    while True:
        buffer = ''
        idC += 1
        nome, idade, cpf_cnpj, medicamento = input(
            'digite o nome, a idade, o cpf/cnpj ,e o produto do cliente (separado por espaços) ').split()
        selc = int(input('digite o tipo de pessoa que é 1-fisica 2-juridica '))
        while not 1 <= selc <= 2:
            selc = int(
                input('valor invalido , digite o tipo de pessoa que é 1-fisica 2-juridica '))
        if selc == 1:
            tipo = 'fisica'
            buffer = ClienteFisico(
                idC, nome, idade, cpf_cnpj, medicamento, tipo)
        elif selc == 2:
            tipo = 'juridica'
            buffer = ClienteJuridico(
                idC, nome, idade, cpf_cnpj, medicamento, tipo)
        clientes.append(buffer)
        fim = (input('deseja cadastrar mais um cliente? [s/n] '))
        if fim.lower() != 's':
            break
    return clientes, idC


def editCliente(clientes):
    print('Alterar informação do cliente')
    idF = int(input('Digite o ID do cliente '))
    flag = False
    for func in clientes:  # percorre a lista de clientes
        if idF == func.get_idC():  # busca pelo ID do cliente a ser alterado
            print('Digite as novas informações do cliente')
            nome, idade, cpf, medicamento = input(
                'digite o nome, a idade, o cpf/cnpj e o produto do cliente (separado por espaços) ').split()
            selc = int(
                input('digite o tipo de pessoa que é 1-fisica 2-juridica '))
            while not 1 <= selc <= 2:
                selc = int(
                    input('valor invalido , digite o tipo de pessoa que é 1-fisica 2-juridica '))
            if selc == 1:
                func.set_cpf(cpf)
                func.set_tipo('fisica')
            elif selc == 2:
                func.set_cpf(cpf)
                func.set_tipo('juridica')
            func.set_nome(nome)
            func.set_idade(idade)
            func.set_medicamento(medicamento)

            flag = True
    if flag == False:
            print("ID não encontrado!")
    return clientes


def delCliente(clientes):
    deletar = int(input('digite a id do cliente que voce quer deletar: '))
    flag = False
    # percorre a lista de funcionários  # percorre a lista de funcionários
    for i,j in enumerate(clientes):
        if deletar == j.get_idC():
            clientes.pop(i)
            flag = True
            print('cliente deletado com sucesso')
    if flag == False:
        print("Id não cadastrado!")
    return clientes


def pesquisaCliente(clientes):
    termo = (input('digite o termo da pesquisa '))
    print('')
    flag=False
    for a in range(len(clientes)):
        if clientes[a].get_nome() == termo or clientes[a].get_cpf() == termo or clientes[a].get_idade() == termo or clientes[a].get_medicamento() == termo or str(clientes[a].get_idC()) == termo or clientes[a].get_tipo() == termo:
            clientes[a].get_info()
            flag=True
    if flag==False:
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
        idM += 1
        nome, validade,preço = input(
            'digite o nome, a validade do produto e o preço de compra ').split()
        selc = int(input('digite o tipo de produto que é 1-medicamento 2-perfume '))
        while not 1 <= selc <= 2:
            selc = int(
                input('valor invalido ,digite o tipo de produto que é 1-medicamento 2-perfume '))
        if selc == 1: #isso está aqui só para iniciar e salvar no cadastro 
            tipo = 'medicamento'
            buffer = Medicamento(idM, nome, validade,preço,tipo)
            buffer.gerarVenda(preço)
        elif selc == 2:
            tipo = 'perfume'
            buffer = Perfume(idM, nome, validade,preço,tipo)
            buffer.gerarVenda(preço)
        medic.append(buffer)
        fim = (input('deseja cadastrar mais um medicamento? [s/n] '))
        if fim.lower() != 's':
            break
    return medic, idM


def editMedic(medic):
    print('Alterar informação do medicamento')
    idM = int(input('Digite o ID do medicamento '))
    flag = False
    for func in medic:  # percorre a lista de medic
        if idM == func.get_idM():  # busca pelo ID do cliente a ser alterado
            print('Digite as novas informações do medicamento')
            nome, validade,preço = input(
             'digite o nome, a validade do medicamento e o preço de compra ').split()
            selc = int(input('digite o tipo de produto que é 1-medicamento 2-perfume '))
            while not 1 <= selc <= 2:
                selc = int(
                    input('valor invalido ,digite o tipo de produto que é 1-medicamento 2-perfume '))
            if selc == 1:
                func.gerarVenda(preço) #isso está aqui só para iniciar e salvar no cadastro 
                func.set_tipo('medicamento')
            elif selc == 2:
                func.gerarVenda(preço)
                func.set_tipo('perfume')
            func.set_nome(nome)
            func.set_validade(validade)
            func.set_preço(preço)
            flag = True
    if flag == False:
        print("ID não encontrado!")
    return medic


def delMedic(medic):
    deletar = int(input('digite a id do produto que voce quer deletar: '))
    flag = False
    # percorre a lista de funcionários  # percorre a lista de funcionários
    for i,j in enumerate(medic):
        if deletar == j.get_idM():
            medic.pop(i)
            flag = True
            print('produto deletado com sucesso')
    if flag == False:
        print("Id não cadastrado!")
    return medic


def pesquisaMedic(medic):
    termo = (input('digite o termo da pesquisa '))
    print('')
    flag=False
    for a in range(len(medic)):
        if medic[a].get_nome() == termo or medic[a].get_validade() == termo or str(medic[a].get_idM()) == termo or medic[a].get_preço() == termo or medic[a].get_tipo() == termo or medic[a].get_venda() == termo or medic[a].get_tipo() == termo:
            medic[a].get_info()
            flag=True
    if flag==False:
            print('termo não encontrado')
    print('')


def printMedic(medic):
    print('')
    for a in range(len(medic)):
        medic[a].get_info()
    print('')


clientes = list()
medic = list()
idC = 0
idM = 0
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
            clientes, idC = cadastroCliente(clientes, idC)
        elif control2 == 2:
            medic, idM = cadastroMedic(medic, idM)
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
