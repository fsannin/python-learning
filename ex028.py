### Jogo da adivinhação v1
### Importamos o sleep e run do asyncio para criar uma pausa no programa, dando a sensação de que o computador está "pensando" no número
from asyncio import sleep, run
### Importamos o random para gerar um número aleatório
import random

### Usamos o async def para definir o código assíncrono, permitindo o uso do await para criar a pausa
async def main():
    num = random.randint(0, 5)
    print('-=---=---=---=---=---=---=---=\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n-=---=---=---=---=---=---=---=')
    guess = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    await sleep(3)
    if guess == num:
        print('Parabéns! Você acertou!')
    else:
        print(f'Você errou! Eu pensei no número {num}.')
### Utilizamos o run para executar a função main, que é a função principal do programa
run(main())
