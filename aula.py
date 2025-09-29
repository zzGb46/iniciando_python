# print("helou")
# print("estou no dba")
# nome = input("Digite seu nome:")
# print(nome)
# nome = "gb"

# print(f"meu nome é {nome}")

# nota_1=int(input("Digite primeira nota"))
# nota_2 = int(input("Digite a segunda nota"))
# nota_3 = int(input("Digite a terceira nota"))
# nota_4 = int(input("Digite a quarta nota"))

# media = (nota_1+nota_2+nota_3+nota_4)/4

# # print(f"a media foi de: {media}")

# if media >= 6:
#     situacao = "aprovado"
# else:
#     situacao = "reprovado"

#     print(f"a media foi {media}")
#     print(f"a situação é {situacao}")

# def divisao(a,b):
#     resultado = a/b
#     return resultado

# resultado_divisao = divisao(3,3)
# print(resultado_divisao)


# def verificar(numero):
#    numero = int(input("insira um numero:"))
#    if numero %2==0:
#         return True
#    else:
#       return False
# SEQUÊNCIA
# texto = "explorando a diversidade de linguagens de programção com Python"
# print(f"tamanho do texto = {len(texto)}")
# print(f"Python in texto = {'Python' in texto}")
# print(f"quantidade de e no texto {texto.count('e')}")
# print(f"as 5 primeiras letras são: {texto[:5]}")

# LISTA
# cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']

# for cor in cores:
#    print(f'Posição = {cores.index(cor)}, cor = {cor}')

# MUTABILIDADE(MAIUSCULO, MINUSCULO)
# # linguagens= ["Python", "Java", "JavaScript", "C", "C#", "Swift", "Go"]

# print("antes do listcomp", linguagens)
# linguagens = [item.lower() for item in linguagens]
# print("\ndepois do listcomp",linguagens)


# A LINHA DE CODIGO ACIMA FUNCIONA COMO UM ENUMERATE COMO NO EXEMPLO ABAIXO:
#    vogais = ["a", "e", "i", "o", "u"]

# for p, x in enumerate(vogais, start=1):
#     print(f"Índice {p} → valor {x}")

# SAIDA:
# Índice 1 → valor a
# Índice 2 → valor e
# Índice 3 → valor i
# Índice 4 → valor o
# Índice 5 → valor u

# Treinando classes python

# class Pessoa:
#     def __init__(self, nome, idade, genero):
#         self.nome = nome
#         self.idade = idade
#         self.genero = genero

# # o metodo cumprimentar retorna uma saudação com o nome da pessoa.
#     def cumprimentar(self):
#         return f"Olá meu nome é {self.nome}"

#     def aniversario(self):
#         self.idade += 1
#         return f"tenho {self.idade}"

# #  cria uma instancia da classe "Pessoa"
# pessoa1 = Pessoa("João", 30, "masculino")

# #    chama o metodo "cumprimentar" na instancia pessoa1 e impreme a saudação.
# print(pessoa1.cumprimentar())

#     #  acessa o atributo idade da instancia pessoa1 e impreme sua idade
# print(f"idade: {pessoa1.idade}")
# # print(pessoa1.aniversario())
#     #  chama o metodo "aniversario" na instancia pessoa1 para aumentar sua idade em 1.
# pessoa1.aniversario()
#     #  acessa o aributo idade atualizado da instancia pessoa1 e impreme a nova idade.
# print(f"nova idade: {pessoa1.idade}")

# class Animal:
#     def __init__(self, nome):
#         self.nome = str(nome)

#     def fazer_barulho(self):
#         pass

# #  herança de animal para cachorro


# class Cachorro(Animal):
#     def fazer_barulho(self):
#         return "latir"
    
#     def __str__(self):
#         return self.nome
#     # herança de animal para cachorro


# class Gato(Animal):
#     def fazer_barulho(self):
#         return "miar"

#     def __str__(self):
#         return self.nome
     

# Criando objetos das classes-filha


# whiskers = Gato("Whiskers")
# rex = Cachorro("Rex")
# # Chamando o método fazer_barulho em objetos

# print(f"{rex} faz: {rex.fazer_barulho()}")
# # saida: "rex fazer: Latir"
# print(f"{whiskers} faz: {whiskers.fazer_barulho()}")
# saida: "whikers faz miar"


# SEGUNDO EXEMPLO HERANÇA CLASSES

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
     return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        #  return super().acelerar(incremento)
        # CARROS PODEM ACELERAR MAIS RAPIDO
        self.velocidade += incremento + self.potencia


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):

        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} km/h"


carro1 = Carro("Toyota", "Corolla", 2022, 150)

# criando objetos o segundo é bicicleta
bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

#   acelerando e verificando o status
carro1.acelerar(50)

bicicleta1.acelerar(20)

# exibindo o status dos veiculos
# status do carro
print("status do carro.")
print(carro1.status())

# status da bicicleta
print("\nStatus da bicicleta")
print(bicicleta1.status())
