from Produto import Produto

class Perfume(Produto):
    def __init__(self, idM,nome, validade,preço,tipo):
        self.venda=0
        super().__init__(idM,nome, validade,preço,tipo)
    
    def gerarVenda(self,preço):
        print('Gerando preço de venda a 500 porcento de lucro')
        self.venda =float(preço)*6
        print('preço de venda: {}'.format(self.venda))
    
    def get_info(self):
         super().get_info()
class Medicamento(Produto):
    def __init__(self, idM,nome, validade,preço,tipo):
        self.venda=0
        super().__init__(idM,nome, validade,preço,tipo)
    def gerarVenda(self,preço):
        print('Gerando preço de venda a 300 porcento de lucro')
        self.venda =float(preço)*4
        print('preço de venda: {}'.format(self.venda))
    def get_info(self):
        super().get_info()