
class Medicamento:
    def __init__(self, idM,nome, validade,preço,tipo):
        self.idM=idM
        self.nome=nome
        self.validade=validade
        self.preço=preço
        self.venda=0
        self.tipo=tipo
    def get_nome(self):
        return self.nome
    def get_validade(self):
        return self.validade
    def get_idM(self):
        return self.idM
    def get_preço(self):
        return self.preço
    def get_venda(self):
        return self.venda
    def get_tipo(self):
        return self.tipo
    
    def gerarVenda(self,preço):
        print('Gerando preço de venda há 300 porcento de lucro')
        self.venda =float(preço)*3
        print('preço de venda: {}'.format(self.venda))
    
    def get_info(self):
        print('id: {} nome: {} validade:{} preço de compra: {} reais preço de venda: {} reais tipo: {}'.format(self.idM,self.nome,self.validade,self.preço,self.venda,self.tipo))
 
    def set_tipo(self,tipo):
        self.tipo = tipo
    def set_nome(self,nome):
        self.nome = nome
    def set_validade(self,validade):
        self.validade = validade
    def set_idM(self,idM):
        self.idM = idM
    def set_preço(self,preço):
        self.preço=preço
    def set_venda(self,venda):
        self.venda=venda
   
        