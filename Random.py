import random

aleatorio= random.randint(1,30)
print (aleatorio)

#jogo
chance= 3
while chance != 0:
    chute= int(input('digite um numero entre 1 a 30: '))

    if chute == aleatorio:
            print('voce acertouu')
            break
    else:
            print(f'errouu, o numero era{aleatorio}, você tem:{chance} chances')
        
    chance -= 1
    if chance == 0:
        print('perdeu')
