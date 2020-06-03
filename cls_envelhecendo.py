class Pessoa:

    def caracteristica_pessoa(self, nome, idade, peso, altura, ano_nascimento):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento

    def idade_atual(self, ano_atual):
        self.ano_atual = ano_atual
        idade = self.ano_nascimento - self.ano_atual
        if idade < 21:
            self.altura += 0.5
        
        return idade
    
    def engordar(self, peso):
        self.peso += peso
