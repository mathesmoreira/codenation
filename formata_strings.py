idade = 25
nome = 'Matheus P Moreira'

#Três jeitos de formatar strings
print('Minha idade é: ' + str(idade))
print('Minha idade é: {}'.format(idade))
print(f'Minha idade é: {idade}')

print(f'Meu nome é {nome} e eu tenho {idade} anos')
print(f'Eu terei {idade + 30} daqui a 30 anos')

#Pegando as 7 primeiras letras do nome e a idade como um numero de 5 digitos
print(f'Meu nome é {nome:.7} e eu tenho {idade:05} anos')

#Print dinheiro
dinheiro = 1.5
print(f'Eu tenho {dinheiro:.2f} reais')

#Print itens de uma lista
lista_escola = ['lápis','caneta','borracha']
print(f'Eu uso o {lista_escola[0]} ou a {lista_escola[1]} para escrever, mas a minha {lista_escola[2]} só apaga rabiscos feitos a {lista_escola[0]}.')
