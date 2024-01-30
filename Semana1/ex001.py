"""
Exercício 1. Cap.3 - EX 4a

Ler uma temperatura em graus Celsius e apresentá-la convertida
em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

tempCelsius = int(input("Informe a temperatura em Graus: "));
tempFahrenheit = float((tempCelsius * 9) / 5 + 32);

print(tempFahrenheit);
