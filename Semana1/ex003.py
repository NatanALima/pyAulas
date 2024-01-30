"""
Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética
(variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno
Reprovado com média”. Informar também, após a apresentação das mensagens, o valor
da média obtida pelo aluno.
"""

"""
Seguindo exatamente como o exercício pede

aluno = str(input('Informe o Nome do Aluno: '));
n1 = int(input('Informe a Primeira nota: '));
n2 = int(input('Informe a Segunda nota: '));
n3 = int(input('Informe a Terceira nota: '));
n4 = int(input('Informe a Quarta nota: '));
media = float((n1 + n2 + n3 + n4) / 4);
if media >= 5:
    print(f'O aluno {aluno} foi aprovado com média {media}');
else:
    print(f'O aluno {aluno} foi reprovado com média {media}');
"""

"Modificando o exercício e tornando-o mais dinâmico"
aluno = str(input('Informe o Nome do Aluno: '));
numNotas = int(input('Quantas notas serão informadas?: '));
notas = [];
for x in range(numNotas):
    notas.append(int(input(f'Insira a nota {x+1}: ')));

media = float((sum(notas)) / len(notas))

if media >= 5:
    print(f'O aluno {aluno} foi aprovado com média {media}');
else:
    print(f'O Aluno {aluno} foi reprovado com média {media}');

