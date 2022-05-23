import os
import random as r

os.system('cls')
nome = input('Digite seu nome : ')
print(f'Seja bem-vindo {nome}! Vamos jogar? ')

lista_de_Palavras = ["banana", "uva", "maça"]
palavra_selecionada = r.choice(lista_de_Palavras).upper()
tam_palavra = len(palavra_selecionada)
palavra_codificada = ['_'] * tam_palavra
qtde_erros = 0

while '_' in palavra_codificada and qtde_erros < 6 :
    print(f'\n sua palavra tem {tam_palavra} letras ...')
    print(f'Erros: {qtde_erros} de 6')
    for letra in palavra_codificada:
        print(letra, end = '')
    print()

    letra_escolhida = input('Digite a letra').upper()
    acertou = False
    for i in range(len(palavra_selecionada)):
        if letra_escolhida == palavra_selecionada[i]:
            palavra_codificada[i] = letra_escolhida
            acertou = True

    if acertou == True:
        print('Parabens! Acertou.')
    else:
        print('Errou, essa letra não existe na palavra')
        qtde_erros = qtde_erros +1

if qtde_erros == 6:
    print('Voce perdeu.. tente novamente')
else:
    print('Parabens ! ! !   voce ganhou!')
print(f'A palavra era: {palavra_selecionada}')
