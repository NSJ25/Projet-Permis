from gpiozero import LED, Button
from time import sleep
from signal import pause 

# Configuration des 4 LEDs
led1 = LED(17)
led2 = LED(18)
led3 = LED(20)
led4 = LED(21)
btn = Button(12, bounce_time=None)

# Fonction pour gérer l'appui sur le bouton
def bouton_appuye():
    # Éteindre toutes les LEDs quand le bouton est pressé
    led1.off()
    led2.off()
    led3.off()
    led4.off()

# Associer la fonction à l'événement d'appui sur le bouton
btn.when_pressed = bouton_appuye

