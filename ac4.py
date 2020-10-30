class Medico:
    def __init__(self, nome, CRM, CPF, RG, telefone, salario):
        self.nome = nome
        self.CRM = CRM
        self.CPF = CPF
        self.RG = RG
        self.telefone = telefone
        self.salario = salario

    def informacoes_medico(self):
        print('-'*30)
        print('\n Dados Médico: ')
        print('Nome: ', self.nome)
        print('CRM: ', self.CRM)



medico = Medico('Rafael Arcanjo de Oliveira', 1903205, 42439207888, 433768575, '(11) 98736-8374', 10000)
medico.informacoes_medico()

class Paciente:
    def __init__(self, nome, RG, CPF, endereco, telefone, datanascimento):
        self.nome = nome
        self.RG = RG
        self.CPF = CPF
        self.endereco = endereco
        self.telefone = telefone
        self.datanascimento = datanascimento


