
for i in range(10):
    print(i)

#Adicionando nomes a lista convidados
num_conv = int(input('Digite o numero de convidado: '))

list_conv = []
for i in range(num_conv):   
    new_conv = input('Digite o nome do convidado: ')
    list_conv.append(new_conv)

#Print de cada convidado na lista
for convidado in list_conv:
    print(convidado + ' esta na lista')

count = 0
while count < 5:
    count = count + 1
    print('Contador:' + str(count))

