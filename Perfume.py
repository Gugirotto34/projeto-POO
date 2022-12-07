from Medicamento import Medicamento

class Perfume(Medicamento):
    def __init__(self, idM,nome, validade,preço,venda,tipo):
        super().__init__(idM,nome, validade,preço,venda,tipo)
    def get_tipo(self):
        return self.tipo
    def set_tipo(self,tipo):
        self.tipo = tipo
    
    def gerarVenda(self,preço):
        print('Gerando preço de venda há 500 porcento de lucro')
        self.venda =float(preço)*5
    
    def get_info(self):
         super().get_info()