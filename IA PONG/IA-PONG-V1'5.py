# CALCULAR POS SABIENDO SU VELOCIDAD

import pyautogui
import keyboard
import time

def calcularPos(prebola,bola):

    #Hallamos tiempo impacto con eje x
    if preBola[0] > bola[0]:
        velX = -525 # 7 * 75
    else : velX = 525 # 7 * 75

    if velX > 0: # Hacia derecha
        tiempoImpacto = (1580-bola[0])/velX
    else: # Hacia izquierda
        tiempoImpacto = (bola[0]+920)/-velX

    #Calculamos en eje y
    if preBola[1] > bola[1]:
        velY = -525 # 7 * 75
    else: velY = 525 # 7 * 75

    posFinalY = velY * tiempoImpacto + bola[1]
    while posFinalY < 80 or posFinalY > 1000:
        if posFinalY < 80: #Se va por arriba
            posFinalY = abs(posFinalY) + 80
        if posFinalY > 980: #Se va por abajo
            posFinalY = 980 - (posFinalY - 980)

    return posFinalY

isRunning = True

impactoEnY = None

preBola = (960,536)

while isRunning:
    
    player = None
    bolapos = None

    #GetEvents
    if keyboard.is_pressed("q"):  
        isRunning = False

    #Screenshot
    im = pyautogui.screenshot()

    #Positions Bola
    for x in range(325,1590,10):
        for y in range(65,1010,10):
            if im.getpixel((x,y)) == (255,255,255):
                bolapos = (x + 10 , y + 10)
                break
        if bolapos : break


    #Prediccion Bola

    if bolapos and not preBola == bolapos: 

        bola = (bolapos[0],bolapos[1])

        impactoEnY = calcularPos(preBola,bola)

    else:  
        bola = preBola
        impactoEnY = 540

    

    #Positions player
    for y in range(60,1020,10):
        if im.getpixel((1586,y)) == (148, 0, 211):
            player = y + 40
            break

    
    #Mover player con impactoEnY
    if player:
        """
        if impactoEnY > player + 40: #para abajO
            pyautogui.keyUp("up")
            pyautogui.keyDown("down")
        elif impactoEnY < player - 40: #para arriba
            pyautogui.keyUp("down")
            pyautogui.keyDown("up")
        """
        if impactoEnY > player + 200: #para abajO
            pyautogui.keyDown("down")
        elif impactoEnY < player - 200 : #para arriba
            pyautogui.keyDown("up")
        elif impactoEnY > player + 30 : #para abajO
            pyautogui.keyUp("up")
            pyautogui.keyDown("down")
            time.sleep(0.005)
            pyautogui.keyUp("down")
        elif impactoEnY < player - 30 : #para arriba
            pyautogui.keyUp("down")
            pyautogui.keyDown("up")
            time.sleep(0.005)
            pyautogui.keyUp("up")
        elif impactoEnY > player + 150 and impactoEnY < player -150:
            pyautogui.keyUp("down")
            pyautogui.keyUp("up")
        """
        else: 
            pyautogui.keyUp("up")
            pyautogui.keyUp("down") 
        """

    preBola = bola

    
    
