#Método estático

class Impressora:
    #Verificando quantidade de folhas na impressora
    def verify(self, num_folhas):
        self.num_folhas = num_folhas
        if self.num_folhas == 0:
            print('Nao tem folhas para imprimir. Por favor coloque mais folhas.')
        else:
            print('Preparando para imprimir. Aguarde...')

    #Print dois tipos de erro   
    def error_no_paper(self):
        return print('Erro na hora de impressao. Número insuficiente de folhas! Por favor, coloque mais folha.')

    def imprimindo(self, paginas):
        self.paginas = paginas
        pag_atual = 0
        for pagina in range(paginas):
            pag_atual += 1
            print(f'Imprimindo página {pag_atual}')
            self.num_folhas -= 1
            self.paginas -= 1
            if self.num_folhas == 0:
                impressora.error_no_paper()
                break
            else:
                print('Folha impressa com sucesso!')
                print('===========================')

#Testando as classes
impressora = Impressora()
impressora.verify(10)
impressora.imprimindo(15)



