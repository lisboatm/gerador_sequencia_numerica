# Ler o valor de entrada N
N = int(input().strip())

# Gerar a sequência de saída
for i in range(1, N + 1):
    # Primeira linha para o número i
    print(i, i ** 2, i ** 3)
    # Segunda linha para o número i
    print(i, i ** 2 + 1, i ** 3 + 1)
