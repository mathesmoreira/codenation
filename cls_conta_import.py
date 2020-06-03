from conta import Conta, Cliente

cliente_1 = Cliente('Matheus','Moreira', 1234 )
cliente_3 = Cliente('Joao', 'Silva', 1235)
conta_1 = Conta('123-4', cliente_1, 1000) #c1 guarda a referencia do objeto Conta
conta_3 = Conta('123-5', cliente_3, 1000)


conta_2 = conta_1  # c2 passa a referenciar o mesmo objeto que c1 referencia

# Acessando através da Conta, o nome do titular.
print(conta_1.titular.cpf) 

#Duas referencias que apontam para o mesmo objeto, Conta.
print(type(conta_1))
print(type(conta_2))
if id(conta_1) == id(conta_2):
    print(f'Eles apontam para a mesma referência: {id(conta_1)}')
else:
    print('Eles não apontam para a mesma referência')

conta_1.deposita(100)
conta_1.saca(50)
conta_1.transfere_para(conta_3,150)
# conta_1.extrato
# conta_3.extrato
conta_1.historico.imprime()