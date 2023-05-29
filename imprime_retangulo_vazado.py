#Exercício 2
#Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
# digite a largura: 10
#digite a altura: 3
##########
#        #
##########
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

print('#' * largura)

for _ in range(altura - 2):
    print('#' + ' ' * (largura-2) + '#')

print('#' * largura)