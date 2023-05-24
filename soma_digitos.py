n = int(input("Digite um número inteiro:"))
i = 0
while n:
    i += n % 10 
    n //= 10 
print(i)