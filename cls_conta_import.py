# Importando do arquivo 'conta.py' duas classes(Conta e Cliente)
from conta import Conta, Cliente

cliente_1 = Cliente('Matheus', 'Moreira', 1234)
cliente_3 = Cliente('Joao', 'Silva', 1235)
# conta_1 guarda a referencia do objeto Conta
conta_1 = Conta('123-4', cliente_1, 1000)
conta_3 = Conta('123-5', cliente_3, 1000)

# conta_2 passa a referenciar o mesmo objeto que conta_1 referencia
conta_2 = conta_1

# Acessando através da Conta, o CPF do titular
print(f'CPF titular: {conta_1.titular.cpf}')

# Mostrando que conta_1 e conta_2 apontam para o mesmo objeto, Conta.
print(type(conta_1))
print(type(conta_2))
if id(conta_1) == id(conta_2):
    print(f'Eles apontam para a mesma referência: {id(conta_1)}')
else:
    print('Eles não apontam para a mesma referência')


# Testando: deposito, saque, transferencia e historico
conta_1.deposita(100)
conta_1.saca(50)
conta_1.transfere_para(conta_3, 150)
conta_1.historico.imprime()
