
from Cliente import Cliente

class ClienteFisico(Cliente):
    def __init__(self,idC, nome, idade,cpf,medicamento,tipo):
        self.cpf=cpf
        self.tipo=tipo
        super().__init__(idC, nome, idade,medicamento)
    def get_cpf(self):
        return self.cpf
    def set_cpf(self,cpf):
        self.cpf = cpf
    def get_tipo(self):
        return self.tipo
    def set_tipo(self,tipo):
        self.tipo = tipo
    def get_info(self):
        super().get_info()
        print(" CPF: {} Pessoa {}".format(self.cpf,self.tipo))

    