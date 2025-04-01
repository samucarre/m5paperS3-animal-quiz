# Juego educativo con batería, aciertos, fallos, botón de apagado y sonidos
import M5
from M5 import *
import time
import random
import sys
from machine import Pin, PWM

M5.begin()
# Configuración del buzzer (frecuencias entre 50-5000 Hz)
buzzer = PWM(Pin(21), freq=1000, duty=0)  # Frecuencia inicial 1000 Hz

# Configuración de pantalla
lcd = M5.Lcd
lcd.setRotation(0)  # Vertical: 540x960
lcd.clear()
lcd.setTextColor(0x000000, 0xFFFFFF)
lcd.setTextSize(2)

# Funciones de sonido con frecuencias válidas
def play_success():
    """Sonido alegre ascendente (frecuencias más bajas)"""
    tones = [
        (262, 0.15),  # Do (C4)
        (330, 0.15),  # Mi (E4)
        (392, 0.3)    # Sol (G4)
    ]
    buzzer.duty(512)  # 50% de volumen
    for freq, duration in tones:
        buzzer.freq(freq)  # Actualizar frecuencia
        time.sleep(duration)
    buzzer.duty(0)

def play_error():
    """Sonido triste descendente"""
    tones = [
        (392, 0.2),   # Sol (G4)
        (330, 0.15),  # Mi (E4)
        (262, 0.25)   # Do (C4)
    ]
    buzzer.duty(512)
    for freq, duration in tones:
        buzzer.freq(freq)
        time.sleep(duration)
    buzzer.duty(0)

# [Resto del código permanece igual...]

animal_list = [
    "Bear.png", "Beaver.png", "Cat.png", "Chick.png", "Chicken.png", "Cow.png", "Crocodile.png",
    "Deer.png", "Dog.png", "Dolphin.png", "Donkey.png", "Duck.png", "Eagle.png", "Elephant.png",
    "Flamingo.png", "Fox.png", "Frog.png", "Giraffe.png", "Goat.png", "Gorilla.png", "Hamster.png",
    "Hedgehog.png", "Hippo.png", "Horse.png", "Lion.png", "Monkey.png", "Mouse.png", "Octopus.png",
    "Owl.png", "Panda.png", "Parrot.png", "Penguin.png", "Piglet.png", "Polar Bear.png", "Rabbit.png",
    "Raccoon.png", "Rooster.png", "Shark.png", "Sheep.png", "Sloth.png", "Snail.png", "Squirrel.png",
    "Tiger.png", "Turtle.png", "Whale.png", "Wolf.png", "Zebra.png"
]

# [Configuraciones de imágenes y variables del juego...]

IMG_W = 250
IMG_H = 250
IMG_X = 150
IMG_Y_START = 180
IMG_Y_GAP = 260

positions = [
    (IMG_X, IMG_Y_START),
    (IMG_X, IMG_Y_START + IMG_Y_GAP),
    (IMG_X, IMG_Y_START + 2 * IMG_Y_GAP)
]

correct_animal = ""
options = []
last_touch = (-1, -1)
last_battery_check = time.ticks_ms()
score = 0
fails = 0

# [Funciones auxiliares...]

def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

def dentro_imagen(x, y, bx, by):
    return bx <= x <= bx + IMG_W and by <= y <= by + IMG_H

def mostrar_bateria():
    try:
        battery = M5.Power.getBatteryLevel()
        lcd.setTextSize(1)
        lcd.setTextColor(0x000000, 0xFFFFFF)
        lcd.fillRect(10, 10, 80, 20, 0xFFFFFF)
        lcd.setCursor(10, 10)
        lcd.print("bat: {}%".format(battery))
    except Exception as e:
        print("Error batería:", e)

def mostrar_puntos():
    lcd.setTextSize(2)
    lcd.setTextColor(0x000000, 0xFFFFFF)
    lcd.fillRect(400, 10, 120, 40, 0xFFFFFF)
    lcd.setCursor(1, 30)
    lcd.print("Score {}".format(score))
    lcd.setCursor(1, 50)
    lcd.print("Fails {}".format(fails))

def mostrar_boton_apagado():
    lcd.drawRect(460, 925, 80, 30, 0x000000)
    lcd.setCursor(475, 935)
    lcd.setTextSize(2)
    lcd.print("OFF")

def apagar_dispositivo():
    lcd.clear()
    lcd.setTextColor(0x000000, 0xFFFFFF)
    lcd.setTextSize(7)
    lcd.setCursor(170, 200)
    lcd.print("Bye!")
    lcd.setTextSize(2)
    lcd.setCursor(30, 270)
    lcd.print("Please hold the power button to turn off")
    buzzer.duty(0)
    while True:
        time.sleep(1)

def mostrar_splash():
    lcd.clear()
    try:
        lcd.drawPng("/flash/splash.png", 0, 0)
    except Exception as e:
        print("Error splash:", e)
        lcd.setCursor(150, 200)
        lcd.setTextSize(12)
        lcd.print("Animal Quiz!")
    time.sleep(3)

def nuevo_juego():
    global correct_animal, options
    lcd.clear()
    mostrar_bateria()
    mostrar_puntos()
    mostrar_boton_apagado()
    lcd.setCursor(150, 30)
    lcd.setTextSize(3)
    lcd.setTextColor(0x000000, 0xFFFFFF)
    lcd.print("Which one is...")
    
    correct_animal = random.choice(animal_list)
    lcd.setCursor(150, 100)
    lcd.setTextSize(4)
    lcd.print(correct_animal.split(".")[0])
    
    opciones_temp = [a for a in animal_list if a != correct_animal]
    shuffle_list(opciones_temp)
    opciones = opciones_temp[:2] + [correct_animal]
    shuffle_list(opciones)
    options.clear()
    options.extend(opciones)
    
    for i in range(3):
        x, y = positions[i]
        try:
            lcd.drawPng("/flash/" + options[i], x, y)
        except Exception as e:
            print("Error imagen:", options[i], ":", e)

# Inicialización
M5.update()
last_touch = (M5.Touch.getX(), M5.Touch.getY())
mostrar_splash()
nuevo_juego()

# Bucle principal
while True:
    M5.update()
    x = M5.Touch.getX()
    y = M5.Touch.getY()

    if (x, y) != last_touch:
        last_touch = (x, y)

        if 460 <= x <= 540 and 925 <= y <= 955:
            apagar_dispositivo()

        for i in range(3):
            bx, by = positions[i]
            if dentro_imagen(x, y, bx, by):
                lcd.fillRect(150, 150, 680, 40, 0xFFFFFF)
                lcd.setCursor(150, 150)
                
                if options[i] == correct_animal:
                    score += 1
                    lcd.setTextColor(0x007700, 0xFFFFFF)
                    lcd.setTextSize(2)
                    lcd.print("Correct!")
                    play_success()
                    time.sleep(1.5)
                    nuevo_juego()
                else:
                    fails += 1
                    lcd.setTextColor(0x770000, 0xFFFFFF)
                    lcd.setTextSize(2)
                    lcd.print("Try again")
                    play_error()
                    mostrar_puntos()
                break

    if time.ticks_diff(time.ticks_ms(), last_battery_check) > 10000:
        last_battery_check = time.ticks_ms()
        mostrar_bateria()

    time.sleep(0.1)