#Funcao que facilita a criacao de "classes" novas
def newClass(nome, atributos):
    cls = {}
    for k,j in atributos.items():
        cls[k] = j
    return cls

#Classe 'Pessoa'
Pessoa = {}

def newPessoa(nome,nascimento):
    new = {}
    new['nome'] = nome
    new['nascimento'] = nascimento
    return new

#Tupla data de hoje
def idade(new,hoje):
    hj_d, hj_m, hj_a = hoje
    nasc_d, nasc_m, nasc_a = new['nascimento']
    idade = hj_a - nasc_a
    return idade

Pessoa = newClass('Pessoa',{'newPessoa':newPessoa, 'idade':idade})

#Criando nova instância
hank = Pessoa['newPessoa']('Hank Moody',(12,12,1970))

print(Pessoa['idade'](hank, (6,11,2020)))
