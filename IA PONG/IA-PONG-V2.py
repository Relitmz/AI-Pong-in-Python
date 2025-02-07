#CALCULAR LAS PREDICCIONES PARA CUELQUIER PONG

import pyautogui
import keyboard
import time

isRunning = True

t0 = time.time()
print("0",0)

preBola = ((960,536), t0 )
impactoEnY = None

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
    t1 = time.time()

    if bolapos and  preBola[0] == bolapos: 
        bola = ((bolapos[0],bolapos[1]),t1)
        print("prebola",preBola,"bola",bola,"impactoEnY",impactoEnY)
        #Hallamos tiempo impacto con eje x
        velX = (bola[0][0]-preBola[0][0])/((bola[1]-preBola[1]))

        if velX > 0: # Hacia derecha
            tiempoImpacto = (1580-bola[0][0])/velX
        else: # Hacia izquierda
            tiempoImpacto = (bola[0][0]+920)/-velX

        #Calculamos en eje y
        velY = (bola[0][1]-preBola[0][1])/(bola[1]-preBola[1])
    
        posFinalY = velY * tiempoImpacto + bola[0][1]
        while posFinalY < 80 and posFinalY > 1000:
            if posFinalY < 80: #Se va por arriba
                posFinalY = abs(posFinalY) + 80
            if posFinalY > 1000: #Se va por abajo
                posFinalY = 1000 - (posFinalY - 1000)

        impactoEnY = posFinalY

        t2 = time.time()

    else: bola = ((preBola[0][0],preBola[0][1]),t1)


    #Positions player
    for y in range(60,1020,10):
        if im.getpixel((1586,y)) == (148, 0, 211):
            player = y + 70
            break

    
    #Mover player con impactoEnY



    preBola = bola

