# Classe Pessoa que retorna a idade da pessoa
class Pessoa:

    def caracteristica_pessoa(self, nome, idade, peso, altura, ano_nascimento):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento

    # Método que retorna a idade da pessoa
    def idade_atual(self, ano_atual):
        self.ano_atual = ano_atual
        idade = self.ano_nascimento - self.ano_atual

        # Pessoa com menos de 21 anos aumentam a altura em 0.5
        if idade < 21:
            self.altura += 0.5

        return idade
