# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

#Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
#>>>lista = [2, 4, 2, 2, 3, 3, 1]
#>>>remove_repetidos(lista)
#[1, 2, 3, 4]
#>>>remove_repetidos([1, 2, 3, 3, 3, 4])
#[1, 2, 3, 4]

#lista = [2, 4, 2, 2, 3, 3, 1]

def remove_repetidos(list):
    l = []
    for x in list:
        if x not in l:
            l.append(x)
    l.sort()
    return l

#print(remove_repetidos(lista))