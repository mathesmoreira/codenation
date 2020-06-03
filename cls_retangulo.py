class Retangulo:
    def area_comodo(self, base, comprimento):
        self.base_comodo = base
        self.comprimento_comodo = comprimento

    def area_piso(self, base = 0, comprimento = 0):
        self.base_piso = base
        self.comprimento_piso = comprimento

    def calcular_area(self, comodo = 0):
        if comodo == 1:
            comodo = 0
            return self.base_comodo*self.comprimento_comodo
        else:
            return self.base_piso*self.comprimento_piso
    
    def calcular_perimetro(self):
        self.perimetro = 2*self.nova_comprimento + 2*self.nova_base


#Criando programa que utiliza classe Retangulo
base = float(input('Digite a medida da base do comodo: '))
comprimento = float(input('Digite a medida da comprimento do comodo: '))

area_retangulo = Retangulo()
area_retangulo.area_comodo(base,comprimento)

#Dimensao de PISOS COM FORMATO RETANGULAR
piso_base = float(input('Digite a base do piso: '))
piso_comprimento = float(input('Digite a comprimento do piso: '))

area_retangulo.area_piso(piso_base,piso_comprimento)

#Calculando area comodo(onde calcular_area recebe 1) e a área de cada piso(onde calcular_area recebe 0)
area_comodo = area_retangulo.calcular_area(1)
area_piso = area_retangulo.calcular_area(0)

#Calculando quantidade de pisos que serão utilizados
quant_pisos = (area_comodo/area_piso)

print(f'A quantidade de pisos que serão utilizados é: {quant_pisos}')

# retangulo = Retangulo()
# retangulo.mudar_lados(base,comprimento)
# retangulo.cal_area_perimetro()
