"""
Escreva expressões algébricas Python correspondentes aos seguintes comandos:

a. A soma dos 5 primeiros inteiros positivos.
b. A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
c. O número de vezes que 73 cabe em 403.
d. O resto de quando 403 é dividido por 73.
e. 2 à 10ª potência.
f. O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
g. O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
"""

# Soma dos 5 Primeiros Números
somaFiveNum = int(1 + 2 + 3 + 4 + 5);
print(f'Soma dos Cinco Primeiros Números: {somaFiveNum}');

# A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
idadeSara = 23;
idadeMark = 19;
idadeFatima = 31;
idadeMedia = round(float((idadeSara + idadeMark + idadeFatima)/3), 2);
print(f'A média das idades será {idadeMedia}');

# O número de vezes que 73 cabe em 403
valueInside = int(403/73);
print(f'O número 73 cabe {valueInside} vezes em 403');

# O resto de quando 403 é dividido por 73
resto = 403 % 73;
print(f'O resto da divisão de 403 por 73 será {resto}')

# 2 à décima potência;
print(f'2 elevado a décima potência é {2**10}')

#O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas)
alturaMarkPol = 57;
alturaSaraPol = 54;
print(f'O valor absoluto da distância entre a altura de Sara e Mark é {alturaMarkPol - alturaSaraPol}')

#O menor preço entre os seguintes preços: R$34,99|R$29,95|R$31,50
precos = [29.95, 34.95, 29.95];
menor = precos[0];

if menor > precos[1]:
    menor = precos[1];
if menor > precos[2]:
    menor = precos[2];
if precos[1] == menor == precos[2]:
    print('Todos os valores são iguais')
else:
    print(f'O menor preço é {menor}')







