#Criando uma calculadora
class calculadora():
    def __init__(self):
        self.bateria = bateria()
        self.entrada = teclascalculadora()
        self.operacoes = operacoes()
        self.display = display()
    def novaoperacao(self,valor1,valor2):
        self.entrada.valorEntrada(valor1,valor2)
        self.bateria.uso()
    def soma(self):
        soma = self.operacoes.soma(self.entrada.getvalor())
        self.bateria.uso()
        self.display.mostratexto(soma)




#Toda vez que usar a calculadora a bateria é consumida 90%
class bateria():
    def __init__(self):
        self.pcbateria = 100
        self.gasto = 0.9

    def uso(self):
        self.pcbateria = self.pcbateria*self.gasto
        self.getbateriafraca()

    def getbateriafraca(self):
        print(f'Seu PC tem {self.pcbateria}% de bateria')
        if (self.pcbateria < 55):
            print('Bateria fraca')
            return True
        else:
            return False


class teclascalculadora():
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
    def valorEntrada(self,v1,v2):
        self.valor1 = v1
        self.valor2 = v2
    def getvalor(self):
        return [self.valor1,self.valor2]

#Calculadora ira realizar duas op. soma e subtracao
class operacoes():
    def soma(self,valores):
        val = 0
        for v in valores:
            val += v
        return val
    def subtracao(self,valores):
        val=0
        for v in valores:
            val -= v
        return val

#Display(Mostrando valores na tela)
class display():
    def __init__(self):
        self.textotela='0'

    def mostratexto(self,textotela):
        self.textotela = textotela
        print(self.textotela)


cal1 = calculadora()
cal1.novaoperacao(10,20)

cal1.soma()

cal1.novaoperacao(14,23)
cal1.soma()