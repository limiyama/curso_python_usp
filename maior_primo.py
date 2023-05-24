#Exercício 2 - Primos
#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
#maior_primo(100)
#97
#maior_primo(7)
#7
n = int(input("Digite um número inteiro maior ou igual a 2:"))

def maior_primo(a):
    primos = []
    for i in range(a):
        c = 0
        for j in range(a):
            if i%(j+1) == 0: 
                c += 1
        if c == 2:
            primos.append(i)
    print(max(primos))

maior_primo(n)
#Exercício 3 - Vogais
#Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
#vogal("a")
#True
#vogal("b")
#False