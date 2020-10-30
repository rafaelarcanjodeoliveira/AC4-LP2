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
        print('\n Dados do Médico: ')
        print ('')
        print('Nome: ', self.nome)
        print('CRM: ', self.CRM)



medico = Medico('Rafael Arcanjo de Oliveira', 1903205, 42439207888, 433768575, '(11) 98736-8374', 10000)
medico.informacoes_medico()

class Quarto:
    def __init__(self, numero, andar):
        self.numero = numero
        self.andar = andar

    def informacoes_paciente(self):
        print('-'*30)
        print('\n Dados do Quarto Paciente: ')
        print('Numero: ', self.numero)
        print('Andar: ', self.andar)

class Paciente():
    def __init__(self, nome, RG, CPF, endereco, telefone, datanascimento):
        self.nome = nome
        self.RG = RG
        self.CPF = CPF
        self.endereco = endereco
        self.telefone = telefone
        self.datanascimento = datanascimento

    def informacoes_paciente(self):
        print('-'*30)
        print('\n Dados do Paciente: ')
        print ('')
        print('Nome: ', self.nome)
        print('CPF: ', self.CPF)
        print('Data de Nascimento: ', self.datanascimento)


quarto = Quarto(10, '1 andar')
quarto.informacoes_paciente()

paciente = Paciente('Joãozinho', 43434343, 99999999999, 'Rua das Lagrimas, 123', '(11) 99999999', '19/02/1999')
paciente.informacoes_paciente()

