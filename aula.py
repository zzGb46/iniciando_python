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
linguagens= ["Python", "Java", "JavaScript", "C", "C#", "Swift", "Go", "Kotlin"]

print("antes do listcomp", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\ndepois do listcomp",linguagens)   
   
   
   
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

