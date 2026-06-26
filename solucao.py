# Lê as três idades informadas pelo usuário
a = int(input())
b = int(input())
c = int(input())

# Soma as três idades e subtrai a maior e a menor
# O valor restante é a idade intermediária (de Camila)
print(a + b + c - max(a, b, c) - min(a, b, c))
