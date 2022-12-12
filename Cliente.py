#classe que cria o cliente e possue as funcoes de edita, cadastrar, e pesquisar
class Cliente:
    def __init__(self,idC, nome, idade,medicamento):
        self.idC=idC
        self.nome=nome
        self.idade=idade
        self.medicamento=medicamento
    def get_idC(self):
        return self.idC
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_medicamento(self):
        return self.medicamento
    def get_info(self):
        print('id: {} nome: {} idade:{}  produto: {}'.format(self.idC,self.nome,self.idade,self.medicamento),end=" ")
    
    def set_idC(self,idC):
        self.idC=idC
    def set_nome(self,nome):
        self.nome = nome
    def set_idade(self,idade):
        self.idade = idade
    def set_medicamento(self,medicamento):
        self.medicamento = medicamento
        