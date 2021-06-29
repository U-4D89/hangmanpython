from random import randint
import os
'''
Este es el juego del ahorcado, para jugarlo debes adivinar
una palabra que se escogera al azar
como jugarlo?
primero, pensare en una palabra
segundo, te dire cuantas letras tiene
tercero, te preguntare por una letra
cuarto, me diras una letra, la que quieras pero debe ser una sola
        luego yo buscare si la letra que me diste esta en la palabra
        que pense, si es asi, la pondre en una lista llamada
        'letras adivinadas', sino la anadire a una lista 'letras erroneas'
        y te quitare un intento, cuantos intentos tienes? [10], te seguire
        preguntando por una sola letra hasta que adivines la palabra letra
        por letra o te quedes sin intentos :C.
quinto, si adivinaste la palabra felicidades, ganaste el juego, si tus intentos
        se acabaron, no te preocupes, te dire la palabra y siempre podras jugar
        de nuevo.


### funciones ##
~ la letra ya esta??? | busca la letra que acabas de ingresar en las dos listas que guardan
                      las letras que ya ingresaste, solo retorna VERDADERO si la letra ya
                      la habias ingresado o FALSO si es una letra nueva, no la habias digi-
                      tado.


~ como va el juego??? | Te mostrara tu proceso:
                        cuantas letras has adivinado
                        cuantas veces te has equivocado
                        si ganaste o perdiste

'''
words = []
letras_adivinadas = []
letras_erroneas = []

intentos = 10
aciertos = 0
veces = 0
gano = False
sin_intentos = False

def progreso():
    clear_program_name = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(clear_program_name)

    print('intentos |', intentos,'|', end='')
    print('         La palabra tiene |', len(palabra_al_azar),'| letras')
    print('')
    print('letras erradas: ',letras_erroneas, end='')
    print('     letras acertadas:', letras_adivinadas)

    if gano == True:
        print('')
        print('Increible! Ganaste!!','La palabra era:', str(palabra_al_azar))
        
    # with open('colgado.txt', 'r', encoding='utf-8-sig') as hangman:
    #     for line in hangman:
    #         print(line)
    if sin_intentos ==  True:
        print('')
        print('Te quedaste sin intentos :(.', 'La palabra era:', palabra_al_azar)

    
    

with open ('palabras.txt', 'r', encoding='utf-8-sig') as word_file:
    for line in word_file:
        lista = list(line)
        lista.remove('\n')
        words.append(lista)

    longw= len(words) 
    n_azar = randint(0,longw - 1)

    palabra_al_azar = (words[n_azar])
       

while intentos > 0 or gano == False:
    letra_ingresada = input('>> Ingresa una letra: ')
    
    if len(letra_ingresada) == 1:
        if letra_ingresada in palabra_al_azar:
            #palabra_al_azar.count(letra_ingresada)
            letras_adivinadas.append(letra_ingresada)
            aciertos +=1
            progreso()

        else:
            letras_erroneas.append(letra_ingresada)
            intentos -= 1

        progreso()

    else:
        print('Intenta con [una] letra')
        intentos -= 1

    if len(palabra_al_azar) == len(letras_adivinadas):
        gano = True
        progreso()
        break

    if intentos == 0:
        sin_intentos = True
        progreso()
        break

    elif len(letras_erroneas) >= len(palabra_al_azar):
        sin_intentos = True
        progreso()
        break