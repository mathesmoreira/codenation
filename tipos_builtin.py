#Declarando lista vazia
lista_vazia = []
print(lista_conv)

#Lista de convidados
lista_conv = ['Josefino','Josefao','Joselito', 'Joana']

#Adicionando, a lista de convidados, um infiltrado
lista_conv.append('Furao')

#Removendo um convidado da lista de nomes
lista_conv.remove('Joselito') 
print(lista_conv)

#Print do nome do ultimo convidado
print(lista_conv[-1])

#Possivel ter string e integer ou float juntos em uma lista
lista_conv.append(40)
print(lista_conv)


#Tuple (Lista imutável, ou seja, sem funcoes como append)
#Porem é possível adicionar duas tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1+tupla2
print(tupla3)


#Dicionario: Mapeamento de chave para valor
dados_pessoais = {'nome':'Josefino', 'cidade':'Pouso Alegre'}
#Print do nome da pessoa pela key
print(dados_pessoais['nome'])
#ADD/Removendo no dicionario
dados_pessoais['idade'] = 25
dados_pessoais['nome_falso'] = 'Josefino, lo cabron'
print(dados_pessoais)
del dados_pessoais['nome_falso']
print(dados_pessoais)