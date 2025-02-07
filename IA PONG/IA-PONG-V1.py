#VERSIÓN SEGUIR POSICION DE Y

import pyautogui
import keyboard
import time

isRunning = True

while isRunning:
    
    player = None
    bola = None

    #GetEvents
    if keyboard.is_pressed("q"):  
        isRunning = False

    #Screenshot
    im = pyautogui.screenshot()

    #t0 = time.time()
    #print("0",0)  

    #Positions Bola
    for x in range(325,1590,10):
        for y in range(65,1010,10):
            if im.getpixel((x,y)) == (255,255,255):
                bola = y + 15
                break
        if bola : break

    #t1 = time.time()
    #print("1",t1-t0)

    #Positions player
    for y in range(60,1020,10):
        if im.getpixel((1586,y)) == (148, 0, 211):
            player = y + 70
            break

    #t2 = time.time()
    #print("2",t2-t0)
    
    if bola and player:

        if bola < player : #BOLA ARRIBA 
            pyautogui.keyUp("down")
            pyautogui.keyDown("up")
    
        elif bola > player : #BOLA ABAJO
            pyautogui.keyUp("up")
            pyautogui.keyDown("down")
            
