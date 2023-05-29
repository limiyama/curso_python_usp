largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

linha = 0

while linha < altura:
    print('#' * (largura))
    linha += 1