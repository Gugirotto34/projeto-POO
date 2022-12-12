from Cliente import Cliente

class ClienteJuridico(Cliente):
    def __init__(self,idC, nome, idade,cnpj,medicamento,tipo):
        self.cnpj=cnpj
        self.tipo=tipo
        super().__init__(idC, nome, idade,medicamento)
    def get_cpf(self): #aqui estpa cpf só como nome para ajudar em algumas funçoes no main
        return self.cnpj
    def set_cpf(self,cnpj):
        self.cnpj = cnpj
    def get_tipo(self):
        return self.tipo
    def set_tipo(self,tipo):
        self.tipo = tipo
    def get_info(self):
        super().get_info()
        print(" Cnpj: {} Pessoa {}".format(self.cnpj,self.tipo))