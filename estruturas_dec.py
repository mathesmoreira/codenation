#Verificando se o usuario é menor de idade
idade  = int(input('Digite sua idade: '))

if idade < 18:
    print('Menor de idade')
else:
    print('Maior de idade')

#Verificando tipo do veiculo
tipo = input('Digite o tipo do veículo: ')
marca = input('Digite a marca do veículo: ')
pot = int(input('Digite a potencia do veículo: '))

dados_veiculo = { 'tipo': tipo, 'marca': marca, 'potencia': pot}

if dados_veiculo['tipo'] == 'moto' and dados_veiculo['marca'] == 'honda':
    print('O veículo é uma moto!')
else:
    print('O veículo não é uma moto!')

if dados_veiculo['tipo'] == 'moto' or dados_veiculo['potencia'] > 120:
    print('Seu veículo é rápido')
else:
    print('Seu veículo não é rápido')

#Parentese prioriza as condicoes dentro dele e depois realiza o restante
if (dados_veiculo['tipo'] == 'moto' and dados_veiculo['marca'] == 'honda') or dados_veiculo['potencia'] > 120:
    print('Seu veículo é muito bom!')


if dados_veiculo['tipo'] == 'moto':
    print('Moto')
elif dados_veiculo['tipo'] == 'carro':
    print('carro')
elif dados_veiculo['tipo'] == 'caminhao':
    print('caminhao')    


#Verificando se a variável possui algum valor
verdad = 'Ao menos 1'
falso = ''
int_verd = 1 # Qquer valor DIFERENTE de zero
int_falso = 0

escolha = #verd, falso, int_verd, int_falso, True, None, [],{}

if escolha:
    print('True')
else:
    print('False')