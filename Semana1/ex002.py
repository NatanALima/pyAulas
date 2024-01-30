"""
Exercício 2

Primeiro, execute a atribuição palavras =
['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a
primeira e a última palavras em palavras, na ordem do dicionário.
"""

palavras = ["taco", "bola", "celeiro", "cesta", "peteca"];

palavra1 = palavras[0];
palavra2 = palavras[len(palavras) - 1];

print(f'A primeira palavra é {palavra1} e a última é {palavra2}');