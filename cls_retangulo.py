#Criando uma classe que calcula a área de um retângulo
class Retangulo:
    def area_comodo(self, base, comprimento):
        self.base_comodo = base
        self.comprimento_comodo = comprimento
        return self.base_comodo*self.comprimento_comodo

    def area_piso(self, base = 0, comprimento = 0):
        self.base_piso = base
        self.comprimento_piso = comprimento
        return self.base_piso*self.comprimento_piso

area_retangulo = Retangulo()

#Criando uma interface que irá utilizar a classe 'Retângulo' para retornar 
#a quantidade de pisos que serão utilizados na área retangular
base = float(input('Digite a medida da base do comodo: '))
comprimento = float(input('Digite a medida da comprimento do comodo: '))
area_comodo = area_retangulo.area_comodo(base,comprimento)

#Dimensao de PISOS COM FORMATO RETANGULAR
piso_base = float(input('Digite a base do piso: '))
piso_comprimento = float(input('Digite a comprimento do piso: '))
area_piso = area_retangulo.area_piso(piso_base,piso_comprimento)

#Calculando quantidade de pisos que serão utilizados
quant_pisos = (area_comodo/area_piso)

#Imprimindo essa quantidade para o usuário
print(f'A quantidade de pisos que serão utilizados é: {quant_pisos}')