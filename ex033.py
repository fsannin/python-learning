### Maior e Menor Número
import asyncio
### Importamos o asyncio para criar um programa assíncrono, permitindo o uso do await para criar pausas no programa, dando a sensação de que o computador está "pensando" nos números
async def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    
    # Verificando maior número através de comparações entre os números usando portas lógicas
    maior = num1
    if num2 >= num1 and num2 >= num3:
        maior = num2
    if num3 >= num1 and num3 >= num2:
        maior = num3
    
    # Verificando menor número, da mesma forma que quando verificamos o maior número,
    menor = num1
    if num2 <= num1 and num2 <= num3:
        menor = num2
    if num3 <= num1 and num3 <= num2:
        menor = num3
    print('\033[0;37;40mPROCESSANDO...\033[m') ### Aqui foi utilizado a formatação ANSI para dar cores ao texto. O código \033[0;37;40m define a cor do texto como branco e o fundo como preto
    await asyncio.sleep(2)
    print(f'O maior número é: {maior}')
    print(f'O menor número é: {menor}')
### Como o asyncio foi importado como um todo, utilizamos o asyncio.run para executar a função main, que é a função principal do programa
asyncio.run(main())