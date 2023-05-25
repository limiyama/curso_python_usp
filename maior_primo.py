def maior_primo(a):
    primos = []

    for i in range(a + 1):
        c = 0

        for j in range(a + 1):
            if i % (j+1) == 0: 
                c += 1

        if c == 2:
            primos.append(i)
    return (max(primos))