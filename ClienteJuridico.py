from Cliente import Cliente

class ClienteJuridico(Cliente):
    def __init__(self,idC, nome, idade,cnpj,medicamento,tipo):
        self.cnpj=cnpj
        self.tipo=tipo
        super().__init__(idC, nome, idade,medicamento)
    def get_cnpj(self):
        return self.cnpj
    def set_cnpj(self,cnpj):
        self.cnpj = cnpj
    def get_info(self):
        super().get_info()
        print(" Cnpj: {} Pessoa {}".format(self.cnpj,self.tipo))