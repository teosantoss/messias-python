# Inicialize o vetor Q com 20 posições
Q = [0] * 20

# Preencha o vetor com números positivos
for i in range(20):
    while True:
        try:
            numero = float(input(f"Digite o valor para Q[{i}]: "))
            if numero > 0:
                Q[i] = numero
                break
            else:
                print("Digite apenas números positivos.")
        except ValueError:
            print("Digite um número válido.")

# Encontre o valor e a posição do maior elemento
maior_valor = Q[0]
maior_posicao = 0
for i in range(1, 20):
    if Q[i] > maior_valor:
        maior_valor = Q[i]
        maior_posicao = i

# Encontre o valor e a posição do menor elemento
menor_valor = Q[0]
menor_posicao = 0
for i in range(1, 20):
    if Q[i] < menor_valor:
        menor_valor = Q[i]
        menor_posicao = i

# Exiba os resultados
print(f"O maior elemento de Q é {maior_valor} e está na posição {maior_posicao}.")
print(f"O menor elemento de Q é {menor_valor} e está na posição {menor_posicao}.")
