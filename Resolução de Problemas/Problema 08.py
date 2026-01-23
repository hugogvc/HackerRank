"""
List Comprehensions

Vamos aprender sobre list comprehensions!
Você recebe três inteiros x, y e z, que representam as dimensões de um cuboide, junto com um inteiro n.

Imprima uma lista com todas as coordenadas possíveis (i, j, k) em uma grade 3D, onde a soma i + j + k não seja igual a n.

Aqui:

0 ≤ i ≤ x

0 ≤ j ≤ y

0 ≤ k ≤ z

Por favor, utilize list comprehensions em vez de vários loops, como exercício de aprendizado.

"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())


coord = [
    [i, j, k]
    for i in range (x + 1)
    for j in range (y + 1)
    for k in range (z + 1)
    if i + j + k != 3
    ]
print(coord)
