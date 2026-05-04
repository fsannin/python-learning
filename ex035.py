### Analisando Triângulos
### Aqui temos um programa que usa matématica básica, condições e portas lógicas para analisar se três segmentos de reta podem formar um triângulo.
r1 = float(input('Digite o comprimento do primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))
### Neste segmento temos as condições para formar um triângulo.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um triângulo!')
else:
    print('Os segmentos acima não formam um triângulo!')